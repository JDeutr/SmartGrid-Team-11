from code.classes import battery, house
<<<<<<< HEAD
from code.algorithms import randomise, dijkstra, simulated_annealing
=======
from code.algorithms import randomise, prim, dijkstra, nearest
>>>>>>> 2b8daba4ea585a591ecafc8bc95f87073ce68f36

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
        
        algorithms={"random" : randomise.randomise_layout,
                    "dijkstra" : dijkstra.dijkstra_algorithm,
<<<<<<< HEAD
                    "sa": randomise.randomise_layout}
=======
                    "nearest" : nearest.nearest,
                    "prim" : prim.prim}
>>>>>>> 2b8daba4ea585a591ecafc8bc95f87073ce68f36
        algorithms[algorithm](self.batteries, self.houses)

        prices={
            "shared": self.price_shared,
            "own": self.price_own
            }
        prices[price_type]()

        if algorithm == "sa":
            simulated_annealing.simulated_annealing(self)


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
            battery_cables = []
            for house in battery.houses:

                cables += house.cables
            self.total_price += battery.price + (cable_price*len(set(cables)))

        return self.total_price
