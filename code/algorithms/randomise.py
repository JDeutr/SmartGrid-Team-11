import random

def randomise_layout(batteries, houses):
    random.shuffle(houses)
    used = set()
    for battery in batteries:
        capacity = battery.capacity
        for house in houses:
            if capacity - house.max_output >=0 and house not in used:
                battery.houses.append(house)
                capacity -= house.max_output
                house.lay_cable(battery.pos_x, battery.pos_y)
                used.add(house)