from pydantic import BaseModel, json, Field

from .components import D6Config, D6Key, D6State, D6Traits, D6Attributes, D6Skills


class D6Character(BaseModel):
    """
    D6 Character Model
    """
    key: D6Key
    traits: D6Traits
    state: D6State
    attributes: D6Attributes
    # skills: D6Skills
    _raw: json

    class Config(D6Config):
        title = 'Character'

