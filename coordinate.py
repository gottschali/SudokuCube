from typing import Generator

class Coordinate:
    """ 3-dimensional coordinate for a 3x3x3 cube raning from -1 to 1 """

    def __init__(self, x : int, y : int, z : int):
        self.x = x
        self.y = y
        self.z = z
        self.coords = (x, y, z)

    def __eq__(self, other : "Coordinate") -> bool:
        return self.coords == other.coords

    def __repr__(self) -> str:
        return f"Coordinate({self.x}, {self.y}, {self.z})"

    def __hash__(self):
        return hash(self.coords)

    def _check_in_bounds(self) -> bool:
        """ Check wether the coordinates are within the predefined range [-1, 1] """
        return all(abs(c) <= 1 for c in self.coords)

    def neighbors(self) -> Generator["Coordinate", None, None]:
        """
        Returns a generator that yields all neigboring coordinates(hare a face)
        and are within bounds.
        """
        deltas = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
        for dx, dy, dz in deltas:
            new_coordinate = Coordinate(self.x + dx, self.y + dy, self.z + dz)
            if new_coordinate._check_in_bounds():
                yield new_coordinate

