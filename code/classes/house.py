class House():
    """_summary_
    """
    def __init__(self, pos_x, pos_y, max_output):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.max_output = max_output
        self.cables = []

    def lay_cable(self, pos_x, pos_y):
        """_summary_

        Args:
            pos_x (_type_): _description_
            pos_y (_type_): _description_
        """
        self.cables.append()