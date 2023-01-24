def nearest(batteries, houses):
    assign(batteries, houses)
    for battery in batteries:
        for house in battery.houses:
            house.lay_cable(battery.pos_x, battery.pos_y)

def assign(batteries, houses):
    for house in houses:
        dist_batteries = {}
        for battery in batteries:
            dist_batteries[battery] = abs(battery.pos_x - house.pos_x) + abs(battery.pos_y - house.pos_y)
        dist_batteries = dict(sorted(dist_batteries.items(), key=lambda item: item[1]))
        for battery in dist_batteries:
            if battery.current_capacity - house.max_output >= 0:
                battery.houses.append(house)
                battery.current_capacity -= house.max_output
                break