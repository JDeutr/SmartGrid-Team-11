class Battery():
    """_summary_
    """
    def __init__(self, pos_x, pos_y, capacity, price=5000):
        """_summary_

        Args:
            pos_x (_type_): _description_
            pos_y (_type_): _description_
            capacity (_type_): _description_
            houses (list): list of houses connected to battery
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.capacity = capacity
        self.current_capacity = capacity
        self.houses = []
        self.price = price

    def check_capacity(self):
        """
        Checks if the capacity of a battery is exceeded and by how much
        """
        load = 0
        for house in self.houses:
            load += house.max_output
        overload = load - self.capacity

        # Only return overload if positive value
        if overload > 0:
            return True

        else:
            return False
