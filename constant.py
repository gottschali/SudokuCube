from collections import namedtuple

# Datastructure for holding the cubes of the SudokuCube
Dice = namedtuple("Dice", ["index", "color"])

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

ORIGINAL_COLORS = tuple(Dice(i, color) for i, color in enumerate([
        CYAN, GREEN, YELLOW, PINK, BLUE, BLACK, RED, GREEN, CYAN, BLUE, BLACK,
        BROWN, GREY, YELLOW, RED, CYAN, BLUE, BROWN, BLACK, RED, GREY, BROWN,
        PINK, GREEN, YELLOW, GREY, PINK
    ]))

# To look up the names back. Numbers are used in the first place to optimize memory
COLOR_MAP = {CYAN : "cyan",
             GREEN : "green",
             YELLOW : "yellow",
             PINK : "pink",
             BLUE : "blue",
             BLACK : "black",
             RED : "red",
             BROWN : "brown",
             GREY : "grey"}

