import matplotlib.pyplot as plt
import numpy as np

def randomise_algorithm_plot(prices, district):
    """
    Runs the randomise_algorithm multiple times and returns a list of costs
    """
    average_cost = sum(prices) / len(prices)
    std_dev = np.std(prices)
    plt.hist(prices, bins = 25)
    plt.xlabel("Cost")
    plt.ylabel("Count")
    plt.title(f"Average cost and standard deviation of randomise algorithm of district {district}")
    plt.show()