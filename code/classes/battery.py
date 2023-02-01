class Battery():
    """
    Battery class
    """
    def __init__(self, pos_x, pos_y, capacity, price=5000):
        """
        Initializes battery class
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
