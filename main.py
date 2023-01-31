from code.classes import grid
from code.algorithms import simulated_annealing
from code.visualisation import visualise, output, distribution
import argparse
import json, copy
from time import process_time

def main(district, algorithm, price_type, amount=1):
    """_summary_
    Args:
        district (_type_): _description_
        algorithm (_type_): _description_
        price_type (_type_): _description_
        amount (int, optional): _description_. Defaults to 1.
    """
    time_start = process_time()
    prices = []
    for i in range(amount):
        smart_grid = grid.Grid(district, algorithm, price_type)
        if algorithm == "sa":
            smart_grid.arrange_cables()
            smart_grid = copy.deepcopy(simulated_annealing.rearrange_houses(smart_grid))
            #smart_grid = copy.deepcopy(simulated_annealing.rearrange_cables(smart_grid))
        prices.append(smart_grid.total_price)

    if amount == 1:
        output.output(smart_grid)
        time_stop = process_time()
        print(time_stop - time_start)
        visualise.visualise(smart_grid, district)
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