from typing import AnyStr, NoReturn, Union, Optional
from collections import deque


class D6CharacterAttribute(object):
    label: AnyStr
    die: int
    _value: int
    _message: deque = deque('initialized', 5)

    def __init__(self,
                 label: AnyStr,
                 value: int = 3,
                 die: Optional[int] = 6):
        """Field"""
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

    @property
    def message(self) -> AnyStr:
        """Internal messages"""
        return self._message[-1]

    @message.setter
    def message(self, msg) -> NoReturn:
        self._message.append(msg)

    def __repr__(self) -> AnyStr:
        return '{}(label={}, value={}, dice={})'.format(self.__class__.__name__,
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

    def __iadd__(self, num: int) -> object:
        self.value = self.value + num
        return self

    def __sub__(self, other: Union[object, int]) -> int:
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

