from collections import deque
from dataclasses import dataclass, field, InitVar
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
    entry: InitVar[int, str]
    label: str = field()
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


@dataclass(order=True)
class CharacterComponent:
    items: list
#
# class D6CharacterComponent(object):
#     """
#
#     """
#     label: str
#     description: str
#
#     def __init__(self, items: list = []):
#         """D6 Character Component"""
#         if items is None:
#             return
#
#         for item in items:
#             self.add_item(item)
#
#     def add_item(self, item: D6CharacterEntry):
#         """
#
#         Parameters
#         ----------
#         item
#         """
#         setattr(self, item.name, item)
#
#     def del_item(self, item: D6CharacterEntry):
#         """
#
#         Parameters
#         ----------
#         item
#         """
#         delattr(self, item.name)
#
#     @property
#     def name(self) -> str:
#         """
#
#         Returns
#         -------
#
#         """
#         return slugify(self.label)
#
#     def values(self) -> list:
#         """
#
#         Returns
#         -------
#
#         """
#         return [getattr(x, 'value') for x in self.__dict__.values()]
#
#     def labels(self) -> list:
#         """
#
#         Returns
#         -------
#
#         """
#         return [getattr(x, 'label') for x in self.__dict__.values()]
#
#     def names(self) -> list:
#         """
#
#         Returns
#         -------
#
#         """
#         return [x for x in self.__dict__.keys()]
#
#     def __str__(self):
#         return '{}'.format(','.join(self.names()))
#
#     def __int__(self):
#         return len(self)
#
#     def __repr__(self):
#         items_repr: list = [repr(x) for x in self.__dict__.values()]
#         return '{}(items=[{}])'.format(self.__class__.__name__, ','.join(items_repr))
#
#     def __getitem__(self, key: str):
#         return self.__dict__.get(key, None)
#
#     def __getattr__(self, key: str):
#         return self.__dict__.get(key, None)
#
#     def __len__(self):
#         return len(self.__dict__)
