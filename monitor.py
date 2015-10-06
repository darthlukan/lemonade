

class monitor:
    panel=False
    name=""
    def __init__(self, name, width, height, xoffset, yoffset):
        self.name = name
        self.width = width
        self.height = height
        self.xoffset = xoffset
        self.yoffset = yoffset

    def __str__(self):
        return "Monitor: " + self.name + "\n" + \
                "Dimensions: " + self.width + "x" + self.height + \
                "+" + self.xoffset + "+" + self.yoffset

