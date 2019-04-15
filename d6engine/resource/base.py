
from collections import deque

from slugify import slugify


def default_verifier(value: [int, str], data: dict) -> bool:
    return True


class D6CharacterEntry(object):
    verifiers: list = [default_verifier]
    _data_list_ = ['label', 'value']

    def __init__(self, label: str, value: [int, str]):
        # initialize queue and value storage
        self._message = deque('C', 5)
        self._value: str

        # set label and value 
        self.label = label
        self.value = value

    def __repr__(self):
        return f'D6CharacterEntry(label={self.label}, value={self.value})'

    @property
    def data(self) -> dict:
        _data: dict = {}
        for item in self._data_list_:
            _data[item] = getattr(self, item)
        return _data 

    @property
    def value(self) -> [int, str]:
        return self._value

    @value.setter
    def value(self, value: [int, str]):
        for verifier in self.verifiers:
            if verifier(value, {'name', self.name}):
                self.message = f'{verifier.__name__} passed'
            else:
                self.message = f'{verifier.__name__} failed'
                raise ValueError(f'{self.message}')
        
        self._value = value

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

    @property
    def name(self):
        """

        Returns
        -------

        """
        return slugify(self.label)

    def __str__(self) -> str:
        return str(self.value)

    def __int__(self) -> int:
        return int(self.value)


class D6CharacterComponent(object):
    """

    """
    label: str
    description: str 

    def __init__(self, items: list = []):
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
    def name(self) -> str:
        """

        Returns
        -------

        """
        return slugify(self.label)

    def values(self) -> list:
        """

        Returns
        -------

        """
        return [getattr(x, 'value') for x in self.__dict__.values()]

    def labels(self) -> list:
        """

        Returns
        -------

        """
        return [getattr(x, 'label') for x in self.__dict__.values()]

    def names(self) -> list:
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
