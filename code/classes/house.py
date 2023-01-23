class House():
    """_summary_
    """
    def __init__(self, pos_x, pos_y, max_output):
        """_summary_

        Args:
            pos_x (_type_): _description_
            pos_y (_type_): _description_
            max_output (_type_): _description_
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.max_output = max_output
        self.cables = []

    def __lt__(self, other):
        """
        Compare two house objects based on their max_output
        """
        return self.max_output < other.max_output

    def lay_cable(self, pos_x, pos_y):
        """_summary_

        Args:
            pos_x (_type_): _description_
            pos_y (_type_): _description_
        """
        cable_x = self.pos_x
        cable_y = self.pos_y
        self.cables.append((self.pos_x, self.pos_y))
        for i in range(abs(self.pos_x - pos_x)):
            if (self.pos_x - pos_x) < 0:
                cable_x += 1
                self.cables.append((cable_x, cable_y))
            else:
                cable_x -= 1
                self.cables.append((cable_x, cable_y))
        for j in range(abs(self.pos_y - pos_y)):
            if (self.pos_y - pos_y) < 0:
                cable_y += 1
                self.cables.append((cable_x, cable_y))
            else:
                cable_y -= 1
                self.cables.append((cable_x, cable_y))
