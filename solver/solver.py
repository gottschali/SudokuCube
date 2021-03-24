from abc import ABC, abstractmethod

from faces import Faces
from coordinate import Coordinate, neighbors, options
from helper import human

class Solver(ABC):

    def __init__(self, sequence):
        self.sequence = sequence # The sequence of the colors
        self.faces = Faces() # Datastructure to model the color constraint
        self.partial = dict() # Contains the partial solutions
        self.solutions = 0
        self.steps = 0

    @property
    @abstractmethod
    def starting_points():
        pass

    def solve(self):
        """ Start solving from every start point """
        for coord in self.starting_points:
            self._solve(coord, 0)
        return self.solutions, self.steps

    def _solve(self, coordinate, depth):
        """ Recursive step """
        # Condition for termination: The cube is completed
        if depth == len(self.sequence) - 1:
            self.solution()
            return True
        self.steps += 1
        color = self.sequence[depth]
        if self.constraints(coordinate, color):
            self.push(coordinate, color, depth)
            # Recursively solve for every neighbor
            for neighbor in neighbors(coordinate):
                if neighbor not in self.partial: # Only use free spaces
                    self._solve(neighbor, depth + 1)
            self.pop(coordinate, color)

    def push(self, coordinate, color, depth):
        """ Step in: Go forward in the sequence and add the step to partial solution """
        self.partial[coordinate] = (color, depth)
        self.faces.push(coordinate, color)

    def pop(self, coordinate, color):
        """ Step out: Go backwards in the sequence and remove the step from the partial solution """
        self.faces.pop(coordinate, color)
        del self.partial[coordinate]

    def solution(self):
        """ Is called when a solution is found """
        self.solutions += 1
        human(self.partial)

    @abstractmethod
    def constraints(self, coordinate, color):
        """ Run checks to limit the recursion """
        return True

class Solver3x3(Solver):
    @property
    def starting_points(self):
        return options

    def constraints(self, coordinate, color):
        """
        Tests if a dice of color at coordinate would violate the constraint that
        on every face of the cube all colors must be distinct
        """
        return not any(color in face for face in self.faces[coordinate])   

class Solver3x3_OS(Solver3x3):
    """ Limits the starting points """
    @property
    def starting_points(self):
        """ 
        All distinct starting coordinates
        Every class of coordinate has sysmmetrical solutions
        """
        return (Coordinate(0, 0, 0),
                Coordinate(0, 0, 1),
                Coordinate(0, 1, 1),
                Coordinate(1, 1, 1))

class Solver3x3_OS_SY(Solver3x3_OS):
    """ Only center is a valid starting point """

    def solve(self):
        # The starting point
        self.push(Coordinate(0, 0, 1), self.sequence[0], 0)
        # Symmetrical first moves
        for c in ((0, 0, 0), (0, 1, 1)):
          self._solve(Coordinate(*c), 1)
        return self.solutions, self.steps

class Solver3x3_OS_SY_BI(Solver3x3_OS_SY):
    """ Makes less steps but uses more time """
    def constraints(self, coordinate, color):
        if not super().constraints(coordinate, color):
            return False
        c = self._components(coordinate)
        return c == 1
    
    def _components(self, coord):
        """ 
        Counts the number of unoccupied regions the cube has if coord is the next step
        If there are more than 1 region its impossible to complete both since you can not change them again.
        """
        self.partial[coord] = None
        stack = []
        visited = {c: False for c in options}
        components = 0
        # Run a DFS on the free die
        for v in options:
            if visited[v] or v in self.partial:
                continue
            components += 1
            stack.append(v)
            while stack:
                n = stack.pop()
                visited[n] = True
                for e in neighbors(n):
                    if not visited[e] and e not in self.partial:
                        stack.append(e)
        del self.partial[coord]
        return components
