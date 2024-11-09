class Opening:
    components_v: dict = {}
    components_h: dict = {}

    def __init__(self, name, w, h):
        self.name = name
        self.w = w
        self.h = h

    width = property(lambda self: self.w)
    height = property(lambda self: self.h)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Window(Opening):
    """
    Has an additional 1x2 at the base, and an additional 1x4 at base.

    """
    components_v = {
        "1X4": 2
    }
    components_h = {
        "1X2": 3,
        "1X4": 1,
        "1X6": 1,
    }


class Door(Opening):
    components_v = {
        "1X4": 2
    }
    components_h = {
        "1X2": 2,
        "1X4": 1,
        "1X6": 1,
    }


class Slider(Door):
    pass