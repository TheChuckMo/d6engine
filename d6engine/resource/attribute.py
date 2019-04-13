"""D6Engine Character Attributes"""
from collections import deque
from typing import AnyStr, NoReturn, Union

from .base import D6CharacterEntry, D6CharacterComponent

D6_CHARACTER_ATTRIBUTE_DEFAULT_DIE: int = 6
D6_CHARACTER_ATTRIBUTE_DEFAULT_VALUE: int = 3


class D6CharacterAttributeEntry(D6CharacterEntry):
    """

    """
    die: int
    _value: int
    _message: deque

    def __init__(self,
                 label: AnyStr,
                 value: int = D6_CHARACTER_ATTRIBUTE_DEFAULT_VALUE,
                 die: int = D6_CHARACTER_ATTRIBUTE_DEFAULT_DIE):
        """Field

        Parameters
        ----------
        label :
        value :
        die :
        """
        self._message = deque('', 5)

        self.label = label
        self.die = die
        self.value = value

    def check(self, item: int) -> bool:
        """Run value check"""
        if item != 0 and item <= self.die:
            return True

        return False

    @property
    def value(self) -> int:
        """Field Value"""
        return self._value

    @value.setter
    def value(self, num: int) -> NoReturn:
        """Set Field Value"""
        if self.check(num):
            self._value = num
            self.message = 'set to {}'.format(num)
        else:
            self.message = 'failed to set {}'.format(num)
            raise ValueError(self.message)

    def __repr__(self) -> AnyStr:
        return '{}(label=\'{}\', value={}, die={})'.format(self.__class__.__name__,
                                                           self.label,
                                                           self.value,
                                                           self.die)

    def __str__(self) -> str:
        return self.label

    def __int__(self):
        return self.value

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
