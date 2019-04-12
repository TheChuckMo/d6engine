from typing import List, AnyStr
from .base import D6CharacterComponent

D6_CHARACTER_COMPONENT_ORDER_DEFAULT: List[str] = ['control',
                                                   'state',
                                                   'advancement',
                                                   'trait',
                                                   'feature',
                                                   'attribute',
                                                   'skill']


class D6CharacterSheet(D6CharacterComponent):
    label: AnyStr = 'Character Sheet'
    description: AnyStr = 'D6Engine Character Sheet'




