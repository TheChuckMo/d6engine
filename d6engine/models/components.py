from pydantic import BaseModel, Field, Json, PositiveInt, conint, constr, EmailStr, HttpUrl
from enum import Enum

from typing import Dict, List, Union


class D6Config:
    validate_assignment = True


class D6Universe(str, Enum):
    Realms = 'realms'
    Fantasy = 'fantasy'
    # Adventure = 'adventure'
    # Space = 'space'


class D6Key(BaseModel):
    """
    key: character management details for server and clients
    """
    id: PositiveInt = Field(..., title='ID', alias='id')
    universe: D6Universe = Field(..., alias='universe')
    player: EmailStr = Field(..., title='Player email')

    class Config(D6Config):
        title = u'Key'


class D6State(BaseModel):
    """
    state: character points for health and advancement
    """
    hp: PositiveInt = Field(..., title='Health Points')
    ap: PositiveInt = Field(..., title='Advancement Points')

    class Config(D6Config):
        title = u'State'


class D6Traits(BaseModel):
    """
    traits: descriptive components of character
    """
    name: str = Field(..., title='Name', max_length=50)
    age: int = Field(..., title='Age', ge=1)
    height: str = Field(..., title='Height', max_length=20)
    weight: PositiveInt = Field(..., title='Weight')
    species: str = Field(..., title='Species', max_length=50)
    hair_color: str = Field(..., title='Hair Color', max_length=25)
    eye_color: str = Field(..., title='Eye Color', max_length=50)
    origin_of_birth: str = Field(..., title='Origin of Birth', max_length=50)
    features: List[str] = Field([], title='Special Features')
    description: str = Field(None, title='Description', max_length=250)
    image_url: HttpUrl = Field(None, title='Image URL')

    class Config(D6Config):
        title = 'Traits'


class D6Attributes(BaseModel):
    """
    attributes: character attributes and points
    """
    dexterity: int = Field(..., title='Dexterity', ge=0, le=6)
    strength: int = Field(..., title='Strength', ge=0, le=6)
    intelligence: int = Field(..., title='Intelligence', ge=0, le=6)
    willpower: int = Field(..., title='Willpower', ge=0, le=6)
    endurance: int = Field(..., title='Endurance', ge=0, le=6)
    perception: int = Field(..., title='Perception', ge=0, le=6)
    social: int = Field(..., title='Social', ge=0, le=6)
    chance: int = Field(..., title='Chance', ge=0, le=6)

    class Config(D6Config):
        title = u'Attributes'


Skill = Dict[str, int]


class D6Skill(BaseModel):
    name: str = Field(..., title='Name')
    value: int = Field(..., title='Value')
    subs: List[Skill] = Field(..., title='Sub Skills')

    class Config(D6Config):
        title = u'Skill'


class D6Skills(BaseModel):
    items: List[D6Skill]

    class Config(D6Config):
        title = u'Skills'
