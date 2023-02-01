import random, copy, math

def rearrange_houses(grid):
    """
    Finds the lowest cost od the smart grid by randomly assigning houses to different 
    batteries. The change is adopted when the cost is lower than the cost of the previous state.
    The state is optimized over many iterations. This algorithm does not yet influence the route
    of the cables to the houses
    """

    # define temperature scheme
    current_temp = 100
    final_temp = 0.01
    alpha = 0.01

    # start with a randomized grid
    initial_grid = grid
    initial_price = initial_grid.price_shared(9)
    print(f" The initial price is {initial_price}")

    # track amount of adopted states and states with overloaded batteries
    overload_count = 0
    adopted = 0

    # assign a random house to a new battery over 5000 iterations
    while current_temp > final_temp:
        # dupicate grid
        new_grid = copy.deepcopy(initial_grid)

        # select a random house and remove it's cable
        rand_battery1, rand_battery2 = random.sample(new_grid.batteries, 2)
        rand_house1 = random.choice(rand_battery1.houses)
        rand_house2 = random.choice(rand_battery2.houses)

        # disconnect houses from batteries
        rand_house1.remove_cable()
        rand_house2.remove_cable()
        rand_battery1.houses.remove(rand_house1)
        rand_battery2.houses.remove(rand_house2)
        
        # connect houses to new cables
        rand_house1.lay_cable(rand_battery2.pos_x, rand_battery2.pos_y)
        rand_house2.lay_cable(rand_battery1.pos_x, rand_battery1.pos_y)

        # assign houses to new battery for cost and capacity calculation
        rand_battery1.houses.append(rand_house2)
        rand_battery2.houses.append(rand_house1)

        # find new price 
        total_price = new_grid.price_shared(9)
        cost_diff = total_price - initial_price

        # check the capacity
        overload = False
        for battery in new_grid.batteries:
            overload += battery.check_capacity()

        # adopt new state if price is lower than initial price
        if cost_diff < 0 and overload == False:
            initial_price = total_price
            initial_grid = copy.deepcopy(new_grid)
            adopted += 1
        
        # if the new solution is not better, accept it with a probability of e^(-cost/temp)
        elif cost_diff > 0 and overload == False:
            if random.uniform(0, 1) < math.exp(-cost_diff / current_temp):
                initial_grid = copy.deepcopy(new_grid)
                adopted += 1

        else:
            overload_count += 1
            
        # decrement the temperature
        current_temp -= alpha

    # visualise grid
    total_price = initial_grid.price_shared(9)
    print(f"After 1000 iterations the total price is {total_price}")
    print(f'overload count is equal to {overload_count}')
    print(f'Number of adopted states is {adopted}')

    return initial_grid