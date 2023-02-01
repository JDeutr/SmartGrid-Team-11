from code.classes import grid
from code.visualisation import visualise
import random
import copy, math

def rearrange_houses(grid):
    """
    Finds the lowest cost of the smart grid by randomly assigning houses to different 
    batteries. The change is adopted when the cost is lower than the cost of the previous state.
    The state is optimized over many iterations. This algorithm does not yet influence the route
    of the cables to the houses
    """

    # start with a randomised grid
    current_temp = 50
    final_temp = 0.01
    alpha = 0.01
    initial_grid = grid
    initial_price = grid.total_price
    print(f" The initial price is {initial_price}")

    # assign a random house to a new battery over 100 iterations
    while current_temp > final_temp:
        # dupicate grid
        new_grid = copy.deepcopy(initial_grid)

        # select a random house and remove it's cable
        rand_house = random.choice(new_grid.houses)
        rand_house.remove_cable()

        # connect house to another battery
        rand_battery = random.choice(new_grid.batteries)
        rand_house.lay_cable(rand_battery.pos_x, rand_battery.pos_y)

        # find new price 
        total_price = new_grid.total_price
        cost_diff = total_price - initial_price

        # adopt new state if price is lower than initial price
        if cost_diff < 0:
            initial_price = total_price
            initial_grid = copy.deepcopy(new_grid)
        
        # if the new solution is not better, accept it with a probability of e^(-cost/temp)
        else:
            if random.uniform(0, 1) < math.exp(-cost_diff / current_temp):
                initial_grid = copy.deepcopy(new_grid)
            
        # decrement the temperature
        current_temp -= alpha

    # visualise grid
    print(f"After 1000 iterations the total price is {total_price}")

    return initial_grid
