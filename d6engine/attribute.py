from typing import NamedTuple, Tuple, AnyStr

D6_ATTRIBUTE_MAX: int = 6
D6_ATTRIBUTE_MIN: int = 1
D6_ATTRIBUTE_DEFAULT: int = 3


class D6Attribute(object):
    label: AnyStr
    _value: int
    min: int
    max: int
    message: AnyStr

    def __init__(self,
                 label: str,
                 value: int = D6_ATTRIBUTE_DEFAULT,
                 max: int = D6_ATTRIBUTE_MAX,
                 min: int = D6_ATTRIBUTE_MIN,
                 message: AnyStr = None):
        """D6 Attribute"""
        self.label = label
        self.max = max
        self.min = min

        # min & max must be set before value
        self.value = value

        self.message = message

    def __repr__(self):
        return '{label}: {value}'.format(label=self.label, value=self._value)

    def __str__(self):
        return self.label

    def __int__(self):
        return self.value

    def check_value(self, num: int) -> bool:
        if num > self.max:
            self.message = 'value {} is larger than max {}'.format(num, self.max)
            return False
        elif num < self.min:
            self.message = 'value {} is smaller than min {}'.format(num, self.min)
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
            raise TypeError(self.message)

    def __add__(self, num: int):
        """add an integer

        self.value
        4
        self = self + 1
        self.value
        5
        """
        add_value: int = self._value + num
        if self.check_value(add_value):
            return D6Attribute(label=str(self), value=add_value)
        else:
            raise TypeError(self.message)

    def __iadd__(self, num: int):
        """add an integer

        self.value
        2
        self += 1
        self.value
        3
        """
        add_value: int = self._value + num
        if self.check_value(add_value):
            self._value = add_value
            return self
        else:
            raise TypeError(self.message)

    def __sub__(self, num: int):
        """subtract an integer

        self.value
        4
        self = self - 1
        self.value
        3
        """
        sub_value: int = self._value - num
        if self.check_value(sub_value):
            return D6Attribute(label=str(self), value=sub_value)
        else:
            raise TypeError(self.message)

    def __isub__(self, num: int):
        """subtract an integer

        self.value
        3
        self -=  1
        self.value
        2
        """
        sub_value: int = self._value - num
        if self.check_value(sub_value):
            self._value = sub_value
            return self
        else:
            raise TypeError(self.message)


class D6AttributeList(object):
    _attribute_list: Tuple[AnyStr] = ('strength', 'dexterity', 'endurance', 'perception',
                                      'intelligence', 'willpower', 'social', 'chance')

    def __init__(self):
        for stat in self._attribute_list:
            setattr(self, stat, D6Attribute(label=stat.capitalize()))


