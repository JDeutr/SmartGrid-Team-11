import matplotlib.pyplot as plt

def visualise(grid, district):
    """_summary_

    Args:
        grid (_type_): _description_
        district (_type_): _description_
    """
    x_house = []
    y_house = []
    x_battery = []
    y_battery = []
    cables = []
    for battery in grid.batteries:
        x_battery.append(battery.pos_x)
        y_battery.append(battery.pos_y)
        for house in battery.houses:
            x_house.append(house.pos_x)
            y_house.append(house.pos_y)
            cables += house.cables

    # plotting the batteries and houses
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xticks(range(51), minor=True)
    ax.set_yticks(range(51), minor=True)
    ax.grid(which='both', alpha=0.3)
    ax.set(xlim=(-1, 51), ylim=(-1, 51))
    for i in range(len(cables)):
        if i == len(cables) - 1:
            break
        if abs(cables[i][0] - cables[i+1][0]) > 1 or abs(cables[i][1] - cables[i+1][1]) > 1:
            continue
        plt.plot([cables[i][0],cables[i+1][0]],[cables[i][1],cables[i+1][1]], 'b-', alpha = 0.6)
    plt.scatter(x_battery, y_battery, marker='P', c='black', label ='Batteries', zorder= 10)
    plt.scatter(x_house, y_house, marker='^', c='red', label ='Houses', zorder= 10)
    plt.xlabel('x coordinates')
    plt.ylabel('y coordinates')
    plt.title(f"District {district}")
    plt.legend(loc='upper right')
    plt.show()