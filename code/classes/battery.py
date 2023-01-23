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
        self.houses = []
        self.price = price
