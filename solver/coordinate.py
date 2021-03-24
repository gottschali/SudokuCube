from collections import namedtuple
import itertools as it

Coordinate = namedtuple("Coordinate", ["x", "y", "z"])

# Differences to a neighbor
deltas = ((1, 0, 0), (-1, 0, 0), (0, 1, 0),
          (0, -1, 0), (0, 0, 1), (0, 0, -1))

# Every coordinate in a 3x3x3 cube
options = tuple(Coordinate(x, y, z) for x, y, z in it.product(range(-1, 2), range(-1, 2), range(-1, 2)))

# Abstract to other sizes           
def neighbors(coordinate):
    x, y, z = coordinate
    for dx, dy, dz in deltas:
        new = Coordinate(x + dx, y + dy, z + dz)
        if all(abs(c) <= 1 for c in new): # Check in bounds
            yield new
