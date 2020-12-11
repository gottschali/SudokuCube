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
