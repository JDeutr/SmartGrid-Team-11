class Battery():
    """_summary_
    """
    def __init__(self, pos_x, pos_y, capacity):
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
        self.price = 5000

    def update_price(self, price_cable):
        """_summary_

        Args:
            price_cable (_type_): _description_
        """
        for house in self.houses:
            self.price += 9*len(house.cables)