from collections import deque
from dataclasses import dataclass, field, InitVar
from collections.abc import Mapping
from typing import Any

from slugify import slugify


def default_verifier(value: [int, str], data: dict) -> bool:
    """ default verifier for character attributes

    Parameters
    ----------
    value :
    data :

    Returns
    -------
    : bool

    """
    return True


@dataclass(order=True, repr=False)
class CharacterEntry:
    label: str = field()
    entry: InitVar[int, str]
    _value: [int, str] = field(init=False, repr=False, compare=False)

    def __post_init__(self, entry: [int, str]):
        self.checks = [default_verifier]
        self._message = deque([], 10)
        self.value = entry

    def __repr__(self):
        return f'{self.__class__.__name__}(entry={self.value}, label={self.label})'

    def __str__(self):
        return f'{self.value}'

    def __int__(self):
        return int(self.value)

    def __bytes__(self):
        return str(self.value).encode('utf-8')

    @property
    def value(self) -> [int, str]:
        """

        Returns
        -------

        """
        return self._value

    @value.setter
    def value(self, value: [int, str]):
        for check in self.checks:
            if check(value, {'name', self.name}):
                self.message = f'{check.__name__} passed'
            else:
                self.message = f'{check.__name__} failed'
                raise ValueError(f'{self.message}')

        self._value = value

    @property
    def name(self):
        return slugify(self.label)

    @property
    def message(self) -> str:
        """Internal messages"""
        return self._message[-1]

    @message.setter
    def message(self, msg: str):
        self._message.append(msg)

    @property
    def messages(self):
        """

        Returns
        -------

        """
        return '::'.join(self._message)


class CharacterComponent(Mapping):
    pass

# @dataclass(order=True)
# class CharacterComponent:
#     items: list

