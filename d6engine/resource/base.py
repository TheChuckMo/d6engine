from collections import deque
from collections.abc import Collection
from datetime import datetime

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
    """Character Entry base

    """
    __slots__ = ['_message', '_label', '_value']
    checks = [default_check]

    def __init__(self, label: str, value: [int, str], checks: list = None):
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

        Returns
        -------

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
        return self._label

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

