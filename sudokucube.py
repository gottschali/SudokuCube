import itertools as it
from sequence import Sequence

class Coordinate:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.coords = (x, y, z)


    @staticmethod
    def options():
        return tuple(Coordinate(x, y, z) for x, y, z in it.product(range(-1, 2), range(-1, 2), range(-1, 2)))

    def __eq__(self, other):
        return self.coords == other.coords

    def __repr__(self):
        return f"Coordinate({self.x}, {self.y}, {self.z})"

    def __hash__(self):
        return hash(self.coords)

    def _check_in_bounds(self):
        return all(abs(c) <= 1 for c in self.coords)

    def neighbors(self):
        deltas = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
        for dx, dy, dz in deltas:
            new = Coordinate(self.x + dx, self.y + dy, self.z + dz)
            if new._check_in_bounds():
                yield new

class Faces(dict):

    def __init__(self):
        self.x = dict(((-1, set()), (1, set())))
        self.y = dict(((-1, set()), (1, set())))
        self.z = dict(((-1, set()), (1, set())))

        self._generate_faces()

    def _get_faces(self, coordinate):
        for axis, coord in zip((self.x, self.y, self.z), coordinate.coords):
            for i in (-1, 1):
                if coord == i:
                    yield (axis, i)

    def _generate_faces(self):
        self._faces = {}
        for coord in Coordinate.options():
            self._faces[coord] = tuple(self._get_faces(coord))


    def test_color_constraint(self, coordinate, color):
        return not any(color in axis[i] for axis, i in self._faces[coordinate])

    def add_to_faces(self, coordinate, color):
        for axis, i in self._faces[coordinate]:
            axis[i].add(color)

    def remove_from_faces(self, coordinate, color):
        for axis, i in self._faces[coordinate]:
            axis[i].remove(color)


class SudokuCube(dict):

    starting_points = {"middle": Coordinate(0, 0, 0),
                       "center": Coordinate(0, 0, 1),
                       "edge": Coordinate(0, 1, 1),
                       "corner": Coordinate(1, 1, 1)}

    def __init__(self):
        self._sequence = Sequence()
        self._faces = Faces()

    def solve(self):
        # Solve from all possible starting points
        self._max_depth = 0
        for coord in SudokuCube.starting_points.values():
            if self._solve(coord, 0):
                mapping_to_sequence(self)
                print(self)
                return True

    def _solve(self, coordinate, depth, verbose=True):
        if verbose:
            if depth > self._max_depth:
                self._max_depth = depth
                print(f"Depth: {self._max_depth}")
                print(self)
        # Update the temporary solution
        self[coordinate] = index, color = self._sequence.push()
        # Condition for termination
        if self._sequence.done():
            return True
        if self._faces.test_color_constraint(coordinate, color):
            self._faces.add_to_faces(coordinate, color)
            # Recursively solve for every neighbor
            for neighbor in coordinate.neighbors():
                # Test that the neigbor is not already occupied
                if neighbor not in self:
                    if self._solve(neighbor, depth + 1):
                        # Propagate a solution
                        return True
            # Remove the colors from the faces
            self._faces.remove_from_faces(coordinate, color)
        # Backtrack
        self._sequence.pop()
        del self[coordinate]

def mapping_to_sequence(sudoku_map):
    hm = sorted(sudoku_map.items(), key=lambda i: i[1].index)
    start = hm[0][0]
    reverse = {v: k for k, v in SudokuCube.starting_points.items()}
    print(f"starting point: {reverse[start]}")
    def direction(coord_a, coord_b):
        if coord_a.x > coord_b.x:
            return "left"
        if coord_a.x < coord_b.x:
            return "right"
        if coord_a.y > coord_b.y:
            return "front"
        if coord_a.y < coord_b.y:
            return "back"
        if coord_a.z > coord_b.z:
            return "up"
        if coord_a.z < coord_b.z:
            return "down"
    for i in range(len(hm) - 1):
        print(f"{direction(hm[i][0], hm[i + 1][0])}, {hm[i + 1][1].color}")

if __name__ == "__main__":
    s = SudokuCube()
    s.solve()
