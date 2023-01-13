import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt


def plot_district(neighbourhood_num):

    # reading the battery and houses CSV
    df_hous = pd.read_csv(f'district_{neighbourhood_num}/district-{neighbourhood_num}_houses.csv')
    df_battery = pd.read_csv(f'district_{neighbourhood_num}/district-{neighbourhood_num}_batteries.csv')

    # Split the 'position' column by the comma and create new 'x' and 'y' columns
    df_battery[['x', 'y']] = df_battery['positie'].str.split(',', expand=True)
    # Convert the new columns to numeric
    df_battery[['x', 'y']] = df_battery[['x', 'y']].apply(pd.to_numeric)

    # x and y coordinates of the houses and the batteries
    x_hous = df_hous['x'].tolist()
    y_hous = df_hous['y'].tolist()
    x_battery = df_battery['x'].tolist()
    y_battery = df_battery['y'].tolist()

    # plotting the batteries and houses
    plt.scatter(x_battery, y_battery, marker='P', c='blue', label ='Batteries')
    plt.scatter(x_hous, y_hous, marker='^', c='red', label ='Houses')

    plt.xlabel('x coordinates')
    plt.ylabel('y coordinates')
    plt.title("Neighbourhood x")
    plt.legend(loc='upper right')

    plt.grid()
    plt.show()

print(plot_district(1))