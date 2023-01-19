from code.classes import battery, house
from code.algorithms import randomise

class Grid():
    def __init__(self, district, algorithm):
        """_summary_
        """
        self.district = district
        self.houses = []
        self.batteries = []
        self.import_batteries(district)
        self.import_houses(district)
        self.total_price = 0
        algorithms={"random" : randomise.randomise_layout}
        algorithms[algorithm](self.batteries, self.houses)
        self.calculate_price()


    def import_houses(self, district):
        with open(f'data/district_{district}/district-{district}_houses.csv', encoding='UTF-8') as house_data:
            next(house_data)
            for row in house_data:
                row = row.replace("\n",'')
                row = row.split(',')
                self.houses.append(house.House(int(row[0]), int(row[1]), float(row[2])))

    def import_batteries(self, district):
        with open(f'data/district_{district}/district-{district}_batteries.csv', encoding='UTF-8') as battery_data:
            next(battery_data)
            for row in battery_data:
                row = row.replace("\n",'')
                row = row.replace('"','').split(',')
                self.batteries.append(battery.Battery(int(row[0]),int(row[1]),float(row[2])))

    def calculate_price(self, cable_price=9):
        for battery in self.batteries:
            self.total_price += battery.price
            for house in battery.houses:
                self.total_price += len(house.cables) * 9