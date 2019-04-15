"""D6Engine Character Attributes"""
from collections import deque
from typing import AnyStr, NoReturn, Union

from .base import D6CharacterEntry, D6CharacterComponent

D6_DEFAULT_DIE: int = 6


def below_one(value: [int], data: dict) -> bool:
    if value > 1:
        return True
    return False


def above_die(value: [int], data: dict) -> bool:
    if value <= data.data('die', 0):
        return True
    return False


class D6CharacterAttributeEntry(D6CharacterEntry):
    verifiers: list = [below_one, above_die]

    def __init__(self, label: str, value: int, die: int = D6_DEFAULT_DIE):
        self.die = die
        self._data_list_.append('die')

        super().__init__(label, value)

    def __repr__(self):
        return f'D6CharacterAttributeEntry({self.label}, {self.value}, {self.die})'

    def __add__(self, other: Union[object, int]) -> int:
        if type(other) is int:
            return self.value + other
        else:
            return self.value + other.value

    def __radd__(self, other: Union[object, int]) -> int:
        if type(other) is int:
            return self.value + other
        else:
            return self.value + other.value

    def __iadd__(self, num: int) -> object:
        self.value = self.value + num
        return self

    def __sub__(self, other: Union[object, int]) -> int:
        if type(other) is int:
            return self.value - other
        else:
            return self.value - other.value

    def __rsub__(self, other: Union[object, int]) -> int:
        if type(other) is int:
            return self.value - other
        else:
            return self.value - other.value

    def __isub__(self, num: int) -> object:
        self.value = self.value - num
        return self

    def __eq__(self, other: object) -> bool:
        return self.value == other.value

    def __ne__(self, other: object) -> bool:
        return self.value != other.value

    def __lt__(self, other: object) -> bool:
        return self.value < other.value

    def __gt__(self, other: object) -> bool:
        return self.value > other.value

    def __ge__(self, other: object) -> bool:
        return self.value >= other.value

    def __le__(self, other: object) -> bool:
        return self.value <= other.value


class D6CharacterAttributeComponent(D6CharacterComponent):
    label: AnyStr = 'Attribute'
    description: AnyStr = 'D6Engine character attributes'
