
from collections import deque
from typing import AnyStr, List, NoReturn

from slugify import slugify


class D6CharacterEntry(object):
    label: AnyStr = 'START'
    _message: deque = deque(label, 5)

    @property
    def message(self) -> AnyStr:
        """Internal messages"""
        return self._message[-1]

    @message.setter
    def message(self, msg):
        self._message.append(msg)

    @property
    def messages(self):
        """

        Returns
        -------

        """
        return '::'.join(self._message)

    @property
    def name(self):
        """

        Returns
        -------

        """
        return slugify(self.label)


class D6CharacterComponent(object):
    """

    """
    label: AnyStr
    description: AnyStr

    def __init__(self, items: List = None):
        """D6 Character Component"""
        if items is None:
            return

        for item in items:
            self.add_item(item)

    def add_item(self, item: D6CharacterEntry):
        """

        Parameters
        ----------
        item
        """
        setattr(self, item.name, item)

    def del_item(self, item: D6CharacterEntry):
        """

        Parameters
        ----------
        item
        """
        delattr(self, item.name)

    @property
    def name(self):
        """

        Returns
        -------

        """
        return slugify(self.label)

    def values(self):
        """

        Returns
        -------

        """
        return [getattr(x, 'value') for x in self.__dict__.values()]

    def labels(self):
        """

        Returns
        -------

        """
        return [getattr(x, 'label') for x in self.__dict__.values()]

    def names(self):
        """

        Returns
        -------

        """
        return [x for x in self.__dict__.keys()]

    def __str__(self):
        return '{}'.format(','.join(self.names()))

    def __int__(self):
        return len(self)

    def __repr__(self):
        items_repr: list = [repr(x) for x in self.__dict__.values()]
        return '{}(items=[{}])'.format(self.__class__.__name__, ','.join(items_repr))

    def __getitem__(self, key: str):
        return self.__dict__.get(key, None)

    def __getattr__(self, key: str):
        return self.__dict__.get(key, None)

    def __len__(self):
        return len(self.__dict__)
