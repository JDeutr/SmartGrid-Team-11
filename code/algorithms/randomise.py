import random

def randomise_layout(batteries, houses):
    random.shuffle(houses)
    used = set()
    for battery in batteries:
        for house in houses:
            if battery.current_capacity - house.max_output >=0 and house not in used:
                battery.houses.append(house)
                battery.current_capacity -= house.max_output
                house.lay_cable(battery.pos_x, battery.pos_y)
                used.add(house)