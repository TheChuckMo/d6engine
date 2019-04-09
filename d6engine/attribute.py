from typing import Tuple, AnyStr


class D6Attribute(object):
    label: str
    _min: int = 1
    _max: int = 6
    _default: int = 3
    _value: int
    _error_message: str

    def __init__(self, label: str, **kwargs):
        self.label = label
        new_value: int = kwargs.get('value', self._default)
        self.value = new_value

    def __repr__(self):
        return '{label}: {value}'.format(label=self.label, value=self._value)

    def __str__(self):
        return self.label

    def __int__(self):
        return self.value

    def check_value(self, num: int) -> bool:
        if num > self._max:
            self._error_message = 'value {} is larger than max {}'.format(num, self._max)
            return False
        elif num < self._min:
            self._error_message = 'value {} is smaller than min {}'.format(num, self._min)
            return False
        else:
            return True

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, num: int):
        if self.check_value(num):
            self._value = num
        else:
            raise TypeError(self._error_message)

    def __add__(self, num: int):
        add_value: int = self._value + num
        if self.check_value(add_value):
            return D6Attribute(label=str(self), value=add_value)
        else:
            raise TypeError(self._error_message)

    def __iadd__(self, num: int):
        add_value: int = self._value + num
        if self.check_value(add_value):
            self._value = add_value
            return self
        else:
            raise TypeError(self._error_message)

    def __sub__(self, num: int):
        sub_value: int = self._value - num
        if self.check_value(sub_value):
            return D6Attribute(label=str(self), value=sub_value)
        else:
            raise TypeError(self._error_message)

    def __isub__(self, num: int):
        sub_value: int = self._value - num
        if self.check_value(sub_value):
            self._value = sub_value
            return self
        else:
            raise TypeError(self._error_message)


class D6AttributeList(object):
    _attribute_list: Tuple[AnyStr] = ('strength', 'dexterity', 'endurance', 'perception',
                                      'intelligence', 'willpower', 'social', 'chance')

    def __init__(self):
        for stat in self._attribute_list:
            setattr(self, stat, D6Attribute(label=stat.capitalize()))


