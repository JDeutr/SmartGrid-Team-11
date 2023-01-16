import random
from code.classes import house

def randomise_layout(battery, houses):
    random.shuffle(houses)
    for house in houses:
        if battery.capacity - house.max_output >= 0:
            battery.houses.append(house)
            battery.capacity -= house.max_output
            house.lay_cable(battery.pos_x, battery.pos_y)
    del houses[:len(battery.houses)]
    