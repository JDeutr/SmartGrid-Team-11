from code.classes import grid
from code.visualisation import visualise
import random
import copy

def simulated_annealing(grid):
    """
    Finds the lowest cost od the smart grid by randomly assigning houses to different 
    batteries. The change is adopted when the cost is lower than the cost of the previous state.
    The state is optimized over many iterations. This algorithm does not yet influence the route
    of the cables to the houses
    """

    # start with a randomised grid
    initial_grid = grid
    initial_price = initial_grid.price_shared(9)
    print(f" The initial price is {initial_price}")

    # assign a random house to a new battery over 100 iterations
    for i in range(200):
        # dupicate grid
        new_grid = copy.deepcopy(initial_grid)

        # select a random house and remove it's cable
        rand_house = random.choice(new_grid.houses)
        rand_house.remove_cable()

        # connect house to another battery
        rand_battery = random.choice(new_grid.batteries)
        rand_house.lay_cable(rand_battery.pos_x, rand_battery.pos_y)

        # find new price 
        total_price = new_grid.price_shared(9)

        # adopt new state if price is lower than 
        if total_price < initial_price:
            initial_price = total_price
            initial_grid = copy.deepcopy(new_grid)

    # visualise grid
    print(f"After {i} iterations the total price is {total_price}")

    return initial_grid
