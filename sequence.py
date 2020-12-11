from collections import namedtuple

CYAN = "cyan"
GREEN = "green"
YELLOW = "yellow"
PINK = "pink"
BLUE = "blue"
BLACK = "black"
RED = "red"
BROWN = "brown"
GREY = "grey"

Dice = namedtuple("Dice", ["index", "color"])

class Sequence(list):
    colors = [
        CYAN,
        GREEN,
        YELLOW,
        PINK,
        BLUE,
        BLACK,
        RED,
        GREEN,
        CYAN,
        BLUE,
        BLACK,
        BROWN,
        GREY,
        YELLOW,
        RED,
        CYAN,
        BLUE,
        BROWN,
        BLACK,
        RED,
        GREY,
        BROWN,
        PINK,
        GREEN,
        YELLOW,
        GREY,
        PINK
    ]

    def __init__(self):
        for i, color in enumerate(Sequence.colors):
            self.append(Dice(i, color))
            self._index = -1

    def __call__(self):
        return self[self._index]

    def push(self):
        self._index += 1
        return self.__call__()

    def pop(self):
        self._index -= 1
        return self.__call__()

    def done(self):
        return self._index == len(Sequence.colors) - 1

