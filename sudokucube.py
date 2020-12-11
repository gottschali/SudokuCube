from coordinate import Coordinate
from faces import Faces
from sequence import Sequence
from helper import human_step_by_step


class SudokuCube(dict):

    def __init__(self):
        self.sequence = Sequence()
        self.faces = Faces()

    def solve(self):
        solutions = 0
        # Solve from all distinct starting points, all others are symmetrical
        for coord in (Coordinate(x, y, z) for x, y, z in ((0, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 1))):
            if self._solve(coord, 0): # A solution is found
                human_step_by_step(self)
                solutions += 1
        print(f"Found {solutions} solutions")
        return solutions

    def _solve(self, coordinate, depth):
        # Step in: go forward in the sequence
        dice = self.sequence.push()
        if self.faces.test_color_constraint(coordinate, dice.color):
            # Step in: set the cube map and add the colors to the faces
            self[coordinate] = dice
            self.faces.add_dice(coordinate, dice.color)
            # Recursively solve for every neighbor
            for neighbor in coordinate.neighbors():
                # Test that the neigbor is not already occupied
                if neighbor not in self:
                    if self._solve(neighbor, depth + 1):
                        # Propagate a solution
                        return True
            # Backtrack: remove the colors from the faces and reset the cube map
            self.faces.remove_dice(coordinate, dice.color)
            del self[coordinate]
        # Condition for termination
        if self.sequence.done():
            # Backtrack
            self.sequence.pop()
            return True
        # Backtrack: go back in the sequence
        self.sequence.pop()


if __name__ == "__main__":
    SudokuCube().solve()
