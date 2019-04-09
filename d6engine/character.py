from .attribute import D6Attribute


class D6Character(object):
    name: str

    attributes = {
        'strength': D6Attribute('Strength')
    }
