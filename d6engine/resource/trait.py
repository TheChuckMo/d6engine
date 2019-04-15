from typing import Union
from collections import deque
from .base import D6CharacterEntry


class D6CharacterTraitEntry(D6CharacterEntry):
    """
    """
    _value: str

    def __init__(self,
                 label: str,
                 value: [int, str]):
        self._message = deque('O', 5)
        self.label = label
        self.value = value
