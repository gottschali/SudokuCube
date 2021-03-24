from enum import IntEnum 
from coordinate import Coordinate

colors = ("cyan", "green", "yellow",
          "pink", "blue", "black",
          "red", "brown", "grey")

Color = IntEnum("Color", colors)

class Seq(tuple):

    def __init__(self, iterable=(), /):
        self = tuple(iterable)
        if not len(self)**(1/3).is_integer():
            raise ValueError("Length of sequence must be a power of three")

OG = Seq(getattr(Color, color) for color in (
        "cyan", "green", "yellow",
        "pink", "blue", "black",
        "red", "green", "cyan",
        "blue", "black", "brown",
        "grey", "yellow", "red",
        "cyan", "blue", "brown",
        "black", "red", "grey",
        "brown", "pink", "green",
        "yellow", "grey", "pink"
    ))
