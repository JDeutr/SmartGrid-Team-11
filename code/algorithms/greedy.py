def greedy(batteries, houses):
    """
    Greedily assigns houses to nearest battery
    """
    assign(batteries, houses)

    # lays the cable between all houses and their assigned battery
    for battery in batteries:
        for house in battery.houses:
            house.lay_cable(battery.pos_x, battery.pos_y)

def assign(batteries, houses):
    """
    Assigns houses to their closest battery if possible
    """

    # iterates through all houses
    for house in houses:

        # dict that tracks distance between house and all batteries
        dist_batteries = {}

        # calculates distance between house and all batteries
        for battery in batteries:
            dist_batteries[battery] = abs(battery.pos_x - house.pos_x) + abs(battery.pos_y - house.pos_y)

        # sorts dist_batteries with in ascending order
        dist_batteries = dict(sorted(dist_batteries.items(), key=lambda item: item[1]))

        # assigns battery to a house if the battery still has capacity
        for battery in dist_batteries:
            if battery.current_capacity - house.max_output >= 0:
                battery.houses.append(house)
                battery.current_capacity -= house.max_output
                break