from code.classes import battery, house
from code.visualisation import visualise as vis
from code.algorithms import randomise
import argparse

def main(district):
    houses = import_houses(district)
    batteries = import_batteries(district)
    for battery in batteries:
        randomise.randomise_layout(battery, houses)
        battery.update_price(9)
        print(battery.price)
    vis.visualise(houses, batteries, district)

def import_houses(district):
    houses = []
    with open(f'data/district_{district}/district-{district}_houses.csv', encoding='UTF-8') as house_data:
        next(house_data)
        for row in house_data:
            row = row.replace("\n",'')
            row = row.split(',')
            houses.append(house.House(int(row[0]), int(row[1]), float(row[2])))
    return houses

def import_batteries(district):
    batteries=[]
    with open(f'data/district_{district}/district-{district}_batteries.csv', encoding='UTF-8') as battery_data:
        next(battery_data)
        for row in battery_data:
            row = row.replace("\n",'')
            row = row.replace('"','').split(',')
            batteries.append(battery.Battery(int(row[0]),int(row[1]),float(row[2])))
    return batteries

if __name__ == "__main__":

    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = "Choose district and type of algorithm")

    # Adding arguments
    parser.add_argument("district", help = "Enter district number")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    main(args.district)