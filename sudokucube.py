import itertools as it
from sequence import Sequence
from helper import human_step_by_step

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

    def __init__(self):
        self._sequence = Sequence()
        self._faces = Faces()

    def solve(self):
        # Solve from all possible starting points
        solutions = 0
        for coord in (Coordinate(x, y, z) for x, y, z in ((0, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 1))):
            if self._solve(coord, 0):
                human_step_by_step(self)
                solutions += 1
        print(f"Found {solutions} solutions")

    def _solve(self, coordinate, depth):
        # Update the temporary solution
        self[coordinate] = index, color = self._sequence.push()
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
        # Condition for termination
        if self._sequence.done():
            # Backtrack
            self._sequence.pop()
            del self[coordinate]
            return True
        # Backtrack
        self._sequence.pop()
        del self[coordinate]


if __name__ == "__main__":
    s = SudokuCube()
    s.solve()
