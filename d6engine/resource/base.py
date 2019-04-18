
from collections import deque
from collections.abc import Iterable, Collection
from dataclasses import dataclass, InitVar, field
from datetime import datetime
from typing import Iterator

from slugify import slugify


class CharacterComponent(Collection):
    pass

    def __len__(self):
        pass

    def __contains__(self, item):
        pass

    def __iter__(self):
        pass

    # def __iter__(self) -> Iterator:
    #     pass


# def __init__(self, items: list) -> None:
    #     self._mapping: list = items

# def __getitem__(self, item):
    #     getattr(self, item, None)
    #
    # def __iter__(self):
    #

def default_verifier(value: [int, str], entry: object) -> bool:
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


@dataclass(repr=False)
class CharacterEntry:
    __slots__ = ['checks', '_message', '_label', '_value']
    entry_label: InitVar[str]
    entry_value: InitVar[int, str]
    entry_checks: InitVar = field(default=[default_verifier])

    def __post_init__(self, entry_label: str, entry_value: [int, str], entry_checks: list):
        self._label = entry_label
        self._value = 0
        self._message = deque([], 10)

        self.checks = entry_checks
        self.value = entry_value

    def __repr__(self):
        return f'{self.__class__.__name__}(entry_label={self.label}, entry_value={self.value})'

    def __str__(self):
        return f'{self.value}'

    def __int__(self):
        return int(self.value)

    def __bytes__(self):
        return str(self.value).encode('utf-8')

    def __eq__(self, other):
        return self.value == other.value

    @property
    def value(self) -> [int, str]:
        """

        Returns
        -------

        """
        return self._value

    @property
    def label(self) -> str:
        return self._label

    @value.setter
    def value(self, value: [int, str]):
        for check in self.checks:
            if check(value, self):
                self.message = f'{check.__name__} passed'
            else:
                self.message = f'{check.__name__} failed'
                raise ValueError(f'{self.message}')
        self._value = value

    @property
    def name(self) -> str:
        return slugify(self._label)

    @property
    def message(self) -> str:
        """Internal messages"""
        return self._message[-1]

    @message.setter
    def message(self, msg: str):
        _stamp = datetime.timestamp(datetime.utcnow())
        _source = self.name
        self._message.append(f'{_source}::{_stamp}::{msg}')

    @property
    def messages(self) -> list:
        """

        Returns
        -------

        """
        return [x for x in self._message]

