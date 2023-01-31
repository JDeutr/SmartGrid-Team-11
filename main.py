from code.classes import grid
from code.algorithms import simulated_annealing
from code.visualisation import visualise, output, distribution
import argparse
import json, copy
from time import process_time

def main(district, algorithm, price_type, amount=1):
    """
    Creates a grid based on the algorithm and district and times all operations before plotting
    """
    # starts time
    time_start = process_time()
   
    prices = []

    # runs the algoritm n amount of times
    for i in range(amount):
        smart_grid = grid.Grid(district, algorithm, price_type)
        if algorithm == "sa":
            smart_grid.arrange_cables()
            smart_grid = copy.deepcopy(simulated_annealing.rearrange_houses(smart_grid))
        prices.append(smart_grid.total_price)

    # checks if amount is 1 and plots if True
    if amount == 1:
        output.output(smart_grid)
        time_stop = process_time()
        print(time_stop - time_start)
        visualise.visualise(smart_grid, district)

    # generates distribution plot if algorithm is random
    elif algorithm == 'random':
        time_stop = process_time()
        print(time_stop - time_start)
        distribution.randomise_algorithm_plot(prices, district)

    else:
        time_stop = process_time()
        print(time_stop - time_start)
    print(f"Average price: {sum(prices)/len(prices)}")


if __name__ == "__main__":

    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = "Choose district and type of algorithm")

    # Adding arguments
    parser.add_argument("district", help = "Enter district number")
    parser.add_argument("amount", help = "Enter amount")
    parser.add_argument("algorithm", help = "Enter algorithm to use")
    parser.add_argument("price_type", help = "Enter price type to use")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    main(args.district, args.algorithm, args.price_type, int(args.amount))