# coding=utf-8
"""base class CharacterEntry CharacterComponent

d6Engine base classes used for resources

"""
from collections import deque, namedtuple
from collections.abc import Collection
from datetime import datetime
from typing import List

from slugify import slugify


class CharacterComponent(Collection):
    _items: namedtuple

    def __init__(self, items: List):
        for item in items:
            self._items.append(item.name, item)

        self._items = items

    def __len__(self):
        len(self._items)

    def __contains__(self, item):
        return item in self._items

    def __iter__(self):
        return self._items

    # def __iter__(self) -> Iterator:
    #     pass


# def __init__(self, items: list) -> None:
#     self._mapping: list = items

# def __getitem__(self, item):
#     getattr(self, item, None)
#
# def __iter__(self):
#

def default_check(value: [int, str], entry: object) -> bool:
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


class CharacterEntry:
    """
    base class character entry


    ...

    Attributes
    ----------
    label: str
        string identifying the entry
    value: int, str
        data held in the entry
    checks: list of func = default_check(value: [int, str], data: dict) -> bool
        list of functions used to verify value before setting
    message: str
        last internal object message

    Methods
    -------
    name: str
        (read-only) auto generated with slugify(label)
    messages: list of str
        list of all internal object messages

    Notes
    -----
    Check functions must take the new value and the entry object as parameters and only return a bool. The checks
    will be run in serial based on the order given until all succeeded or a check fails by returning a False. If
    a test fails an exception will be raised, if all pass the new value will be set. Each check and the final status
    is stored as a message on the object.

    .. def name(value: [int, str], entry: object) -> bool
    ..    if entry.name != 'something':
    ..        return False
    ..    else:
    ..        return True


    """
    __slots__ = ['_message', '_label', '_value']
    checks = [default_check]

    def __init__(self, label: str, value: [int, str], checks: list = None):
        """
        Initiate character entry object

        Parameters
        ----------
        label : str
        value : [int, str]
        checks : list(func) optional
        """
        self._value: [int, str]
        self._label = label
        self._message = deque([], 50)

        if type(checks) is list:
            self.checks.extend(checks)

        self.value = value

    def __repr__(self):
        return f'{self.__class__.__name__}(label={self.label}, value={self.value})'

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
        data stored information

        Returns
        -------
        [int, str]
        """
        return self._value

    @value.setter
    def value(self, value: [int, str]):
        for check in self.checks:
            if check(value, self):
                self.message = f'{check.__name__} passed for {value}'
            else:
                self.message = f'{check.__name__} failed for {value}'
                raise ValueError(f'{self.message}')
        self._value = value
        self.message = f'{self.name} set to {self.value}'

    @property
    def label(self) -> str:
        """
        string to identify data stored

        *read-only*

        Returns
        -------
        str
        """
        return self._label

    @property
    def name(self) -> str:
        """
        entry name: slugify(label)

        *read-only*

        Returns
        -------
        str
        """
        return slugify(self._label)

    @property
    def message(self) -> str:
        """
        last internal entry message (action)

        Returns
        -------
        str
        """
        return self._message[-1]

    @message.setter
    def message(self, msg: str):
        _stamp = datetime.timestamp(datetime.utcnow())
        _source = self.name
        self._message.append(f'{_source}::{_stamp}::{msg}')

    @property
    def messages(self) -> list:
        """
        list of all internal messages (actions)

        Returns
        -------
        list(str)
        """
        return [x for x in self._message]

