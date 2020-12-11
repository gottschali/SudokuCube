import itertools as it

from coordinate import Coordinate

class Faces(dict):
    """
    For every of the six faces of a cube a set is kept with all colors that are part of the site.
    add_dice: Add new dices with
    remove_dice: To remove a dice
    test_color_constraint: Test if a the constraint is violated
    """

    coordinate_options = tuple(Coordinate(x, y, z) for x, y, z in it.product(range(-1, 2), range(-1, 2), range(-1, 2)))

    def __init__(self):
        self.x = dict(((-1, set()), (1, set())))
        self.y = dict(((-1, set()), (1, set())))
        self.z = dict(((-1, set()), (1, set())))
        self._generate_faces()

    def __get_faces(self, coordinate : Coordinate):
        for axis, coord in zip((self.x, self.y, self.z), coordinate.coords):
            for i in (-1, 1):
                if coord == i:
                    yield (axis, i)

    def _generate_faces(self):
        """ initialize self such that self[Coordinate] -> Tuple[[self.x, self.y, self.z], [-1, 1]] """
        for coord in self.coordinate_options:
            self[coord] = tuple(self.__get_faces(coord))

    def test_color_constraint(self, coordinate : Coordinate, color) -> bool:
        """
        Tests if a dice of color at coordinate would violate the constraint that
        on every face of the cube all colors must be distinct
        """
        return not any(color in axis[i] for axis, i in self[coordinate])

    def add_dice(self, coordinate : Coordinate, color):
        """ Adds the color to every face coordinate is a part of """
        for axis, i in self[coordinate]:
            axis[i].add(color)

    def remove_dice(self, coordinate : Coordinate, color):
        """ Removes the color from every face coordinate is a part of """
        for axis, i in self[coordinate]:
            axis[i].remove(color)
