from code.classes import battery, house
import pandas as pd

def import_data(district):
    return import_houses(district), import_batteries(district)

def import_houses(district):
    houses = []
    with open(f'data/district_{district}/district-{district}_houses.csv', encoding='UTF-8') as house_data:
        data = pd.read_csv(house_data, names=['x','y','max_output'])
        for index, rows in data.iterrows():
            if index == 0:
                continue
            houses.append(house.House(rows['x'], rows['y'], rows['max_output']))
    print(houses[1].pos_x)

def import_batteries(district):
    batteries=[]
    with open(f'data/district_{district}/district-{district}_batteries.csv', encoding='UTF-8') as battery_data:
        data = pd.read_csv(battery_data, names=['pos', 'capaciteit'])
        for index, rows in data.iterrows():
            if index == 0:
                continue
            pos = rows['pos'].split(',')
            batteries.append(battery.Battery(pos[0], pos[1], rows['capaciteit']))
    print(batteries[1].pos_x)

import_data('1')