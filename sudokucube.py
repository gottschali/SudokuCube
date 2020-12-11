from coordinate import Coordinate
from faces import Faces
from sequence import Sequence
from helper import human_step_by_step


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
            self._faces.add_dice(coordinate, color)
            # Recursively solve for every neighbor
            for neighbor in coordinate.neighbors():
                # Test that the neigbor is not already occupied
                if neighbor not in self:
                    if self._solve(neighbor, depth + 1):
                        # Propagate a solution
                        return True
            # Remove the colors from the faces
            self._faces.remove_dice(coordinate, color)
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
    SudokuCube().solve()
