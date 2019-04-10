from typing import Dict, AnyStr, Any, List, Optional
import yaml
import os

D6_ATTRIBUTE_MAX: int = 6
D6_ATTRIBUTE_MIN: int = 1
D6_ATTRIBUTE_DEFAULT: int = 3


def load_attributes() -> List:
    attr_file = os.path.join(os.path.dirname(__file__), 'data/attributes.yaml')
    attr_data: List

    with open(attr_file) as data:
        attr_data = yaml.safe_load_all(data)

    return attr_data


class D6AttributeList(object):

    def __init__(self, attributes: List):
        for stat in attributes:
            self.add_attribute(attribute=stat)

    def add_attribute(self, attribute: Dict):
        attr_name: str = attribute.get('name')
        setattr(self, attr_name, D6Attribute(label=attribute.get('label', attr_name.capitalize()),
                                             value=attribute.get('value', D6_ATTRIBUTE_DEFAULT),
                                             max=attribute.get('max', D6_ATTRIBUTE_MAX),
                                             min=attribute.get('min', D6_ATTRIBUTE_MIN),
                                             description=attribute.get('description')))

    def values(self):
        return [getattr(x, 'value') for x in self.__dict__.values()]

    def labels(self):
        return [getattr(x, 'label') for x in self.__dict__.values()]

    def keys(self):
        return [x for x in self.__dict__.keys()]

    def get(self, item: str):
        return getattr(self, item, None)


class D6Attribute(object):
    label: AnyStr
    description: AnyStr
    _value: int
    min: int
    max: int
    message: AnyStr

    def __init__(self,
                 label: str,
                 value: int = D6_ATTRIBUTE_DEFAULT,
                 max: int = D6_ATTRIBUTE_MAX,
                 min: int = D6_ATTRIBUTE_MIN,
                 description: AnyStr = None,
                 message: AnyStr = None):
        """D6 Attribute"""
        self.label = label
        self.description = description

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


