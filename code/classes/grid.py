from code.classes import battery, house
from code.algorithms import randomise, prim, dijkstra, nearest, simulated_annealing
import copy

class Grid():
    def __init__(self, district, algorithm, price_type):
        """_summary_
        """
        self.district = district
        self.houses = []
        self.batteries = []
        self.import_batteries(district)
        self.import_houses(district)
        self.total_price = 0
        self.price_type = price_type
        self.cables = []
        
        algorithms={"random" : randomise.randomise_layout,
                    "nearest" : dijkstra.dijkstra_algorithm,
                    "sa": randomise.randomise_layout,
                    "greedy" : nearest.nearest,
                    "prim" : prim.prim}
                    
        algorithms[algorithm](self.batteries, self.houses)

        # if algorithm == "sa":
        #     self.arrange_cables()
        #     self = copy.deepcopy(simulated_annealing.rearrange_houses(self))
        #     simulated_annealing.rearrange_cables(self)

        prices={
            "shared": self.price_shared,
            "own": self.price_own
            }
        prices[price_type]()
   

    def import_houses(self, district):
        """_summary_

        Args:
            district (_type_): _description_
        """
        with open(f'data/district_{district}/district-{district}_houses.csv', encoding='UTF-8') as house_data:
            next(house_data)
            for row in house_data:
                row = row.replace("\n",'')
                row = row.split(',')
                self.houses.append(house.House(int(row[0]), int(row[1]), float(row[2])))

    def import_batteries(self, district):
        """_summary_

        Args:
            district (_type_): _description_
        """
        with open(f'data/district_{district}/district-{district}_batteries.csv', encoding='UTF-8') as battery_data:
            next(battery_data)
            for row in battery_data:
                row = row.replace("\n",'')
                row = row.replace('"','').split(',')
                self.batteries.append(battery.Battery(int(row[0]),int(row[1]),float(row[2])))

    def price_own(self, cable_price=9):
        """_summary_

        Args:
            cable_price (int, optional): _description_. Defaults to 9.
        """
        for battery in self.batteries:
            cables = 0
            for house in battery.houses:
                cables += len(house.cables) - 1
            self.total_price += battery.price + (cables * 9)


    def price_shared(self, cable_price=9):
        """_summary_

        Args:
            cable_price (int, optional): _description_. Defaults to 9.
        """
        self.total_price = 0
        for battery in self.batteries:
            cables = []
            for house in battery.houses:
                cables += house.cables
            self.total_price += battery.price + (cable_price*(len(set(cables))))

        return self.total_price

    def arrange_cables(self):
        for house in self.houses:
            for cable in house.cables:
                self.cables.append(cable)
                cables = set(self.cables)
                self.cables = list(cables)