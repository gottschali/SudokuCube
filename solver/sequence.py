from typing import Iterable

from constant import *


class Sequence(list):
    """ Represents a SudokuCube sequence """

    def __init__(self, color_sequence : Iterable[Dice] = ORIGINAL_COLORS):
        """ Accepts an optional color_sequence """
        self._index = -1
        self.extend(color_sequence)

    def _front(self) -> Dice:
        """ Returns the current dice """
        return self[self._index]

    def push(self) -> Dice:
        """ Move one dice forward in the sequence and return the new current """
        self._index += 1
        return self._front()

    def pop(self) -> Dice:
        """ Move one dice backwards in the sequence and return the new current """
        self._index -= 1
        return self._front()

    def done(self) -> bool:
        """ The current dice is the last of the sequence """
        return self._index == len(self) - 1

