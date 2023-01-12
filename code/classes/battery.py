class Battery():
    """_summary_
    """
    def __init__(self, pos, capacity):
        """_summary_

        Args:
            pos_x (_type_): _description_
            pos_y (_type_): _description_
            capacity (_type_): _description_
            houses (list): list of houses connected to battery
        """
        self.pos = pos
        self.capacity = capacity
        self.houses = []
        self.price = 0

    def assign_houses(self, district):
        """_summary_

        Args:
            houses (_type_): _description_
        """
        for house in district:
            self.houses.append(house)
        return 'lol'
        # for house in houses:
        #     Iets met nearest neighbour

    def manhattan_distance(self, house):
        """_summary_

        Args:
            house (_type_): _description_

        Returns:
            distance: manhattan distance
        """
        return abs(self.pos[0] - house.pos[1]) + abs(self.pos[0] - house.pos[1])

    def plot(self):
        """_summary_
        """
        # Plots battery and accompanying houses

    def lay_cables(self):
        """_summary_
        """
        # Lay cable for each house

    def add_price(self, price_cable):
        """_summary_

        Args:
            price_cable (_type_): _description_
        """
        for house in self.houses:
            self.price += house.cables * price_cable