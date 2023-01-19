from code.classes import grid
from code.visualisation import visualise, output
import argparse
import json

def main(district, algorithm, price_type, amount=1):
    total_price = 0
    for i in range(amount):
        smart_grid = grid.Grid(district, algorithm, price_type)
        total_price += smart_grid.total_price
    if amount == 1:
        output.output(smart_grid)
        visualise.visualise(smart_grid, district)
    print(f"Average price: {total_price/amount}")


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