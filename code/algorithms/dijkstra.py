import heapq

def dijkstra_algorithm(batteries, houses):
    """
    Assigns houses to batteries using a nearest algorithm, inspired by Dijkstra. Uses 
    a priority queue to assign houses, finds the closest battery to the current house
    and assigns that house to the that battery. Stops when all houses are assigned.
    """
    # Make a dictionary of batteries to their x, y coordinates
    battery_coordinates = {battery: (battery.pos_x, battery.pos_y) for battery in batteries}
    # Make a priority queue for dijkstra algorithm
    priority_queue = []
    # Make a dictionary of house to its assigned battery
    house_to_battery = {}
    # Make a dictionary of battery to its remaining capacity
    battery_remaining_capacity = {battery: battery.capacity for battery in batteries}

    # Add each house to the priority queue
    for house in houses:
        heapq.heappush(priority_queue, (0, house))

    # Run dijkstra algorithm
    while priority_queue:
        distance, current_house = heapq.heappop(priority_queue)

        # Check if the current house has already been assigned to a battery
        if current_house in house_to_battery:
            continue

        # Find the closest battery to the current house
        closest_battery = None
        closest_distance = float('inf')
        for battery in batteries:
            if battery_remaining_capacity[battery] >= current_house.max_output:
                distance = (abs(battery_coordinates[battery][0] - current_house.pos_x) + 
                            abs(battery_coordinates[battery][1] - current_house.pos_y))
                if distance < closest_distance:
                    closest_battery = battery
                    closest_distance = distance

        # Assign the current house to the closest battery
        if closest_battery:
            house_to_battery[current_house] = closest_battery
            battery_remaining_capacity[closest_battery] -= current_house.max_output
            current_house.lay_cable(closest_battery.pos_x, closest_battery.pos_y)
            closest_battery.houses.append(current_house)
