from code.classes import battery, house
import pandas as pd

def import_houses(file):
    houses = []
    with open(f'data/district_1/{file}') as house_data:
        data = pd.read_csv(house_data, names=['pos', 'max_output'])
    for index, rows in data.iterrows():
        if index == 0:
            continue
        houses.append(house.House(rows['pos'], rows['max_output']))
    print(houses[1].pos + " " + houses[2].max_output)

def import_batteries():
    return "lol"

import_houses('district-1_batteries.csv')
