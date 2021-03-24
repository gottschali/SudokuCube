from coordinate import Coordinate, options


class Faces(dict):
    """
    For every of the six faces of a cube a set is kept with all colors that are part of the site.
    add_dice: Add new dices with
    remove_dice: To remove a dice
    test_color_constraint: Test if a the constraint is violated
    """

    def __init__(self):
        self.x = dict(((-1, set()), (1, set())))
        self.y = dict(((-1, set()), (1, set())))
        self.z = dict(((-1, set()), (1, set())))
        self._generate_faces()

    def _generate_faces(self):
        for coord in options:
            self[coord] = tuple(self.__generate_faces(coord))

    def __generate_faces(self, coordinate : Coordinate):
        for axis, c in zip((self.x, self.y, self.z), coordinate):
            for i in (-1, 1):
                if c == i:
                    yield axis[i]

    def push(self, coordinate : Coordinate, color):
        """ Adds the color to every face coordinate is a part of """
        for face in self[coordinate]:
            face.add(color)

    def pop(self, coordinate : Coordinate, color):
        """ Removes the color from every face coordinate is a part of """
        for face in self[coordinate]:
            face.remove(color)