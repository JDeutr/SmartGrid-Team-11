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
