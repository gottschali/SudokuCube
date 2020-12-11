from collections import namedtuple
from typing import Iterable

# Define constants for the colors of the dice
CYAN = 1
GREEN = 2
YELLOW = 3
PINK = 4
BLUE = 5
BLACK = 6
RED = 7
BROWN = 8
GREY = 9

# To look up the names back. Numbers are used in the first place to optimize memory
color_map = {CYAN : "cyan",
             GREEN : "green",
             YELLOW : "yellow",
             PINK : "pink",
             BLUE : "blue",
             BLACK : "black",
             RED : "red",
             BROWN : "brown",
             GREY : "grey"}

ORIGINAL_COLORS = tuple(Dice(i, color) for i, color in enumerate([
        CYAN, GREEN, YELLOW, PINK, BLUE, BLACK, RED, GREEN, CYAN, BLUE, BLACK,
        BROWN, GREY, YELLOW, RED, CYAN, BLUE, BROWN, BLACK, RED, GREY, BROWN,
        PINK, GREEN, YELLOW, GREY, PINK
    ]))

Dice = namedtuple("Dice", ["index", "color"])

class Sequence(list):
    """ Represents a SudokuCube sequence """

    def __init__(self, color_sequence : iterable[dice] = ORIGINAL_COLORS):
        """ Accepts an optional color_sequence """
        self._index = -1
        self.extend(color_sequence)

    def _front(self) -> Dice:
        """ Returns the current dice """
        return self[self._index]

    def push(self) -> Dice:
        """ Move one dice forward in the sequence and return the new current """
        self._index += 1
        return self._front()

    def pop(self) -> Dice:
        """ Move one dice backwards in the sequence and return the new current """
        self._index -= 1
        return self._front()

    def done(self) -> bool:
        """ The current dice is the last of the sequence """
        return self._index == len(self) - 1

