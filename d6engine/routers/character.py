from fastapi import APIRouter
from ..models.character import D6Character
from ..models.components import D6Key

router = APIRouter()


@router.get("/character/{id}", response_model=D6Character, tags=["character"])
async def get_character(did: int, character: D6Character):
    """
    GET get character from id
    :param did:
    :param character:
    :return:
    """
    character = {
        "key": {
            "id": 0,
            "universe": "realms",
            "player": "user@example.com"
        },
        "traits": {
            "name": "string",
            "age": 0,
            "height": "string",
            "weight": 0,
            "species": "string",
            "hair_color": "string",
            "eye_color": "string",
            "origin_of_birth": "string",
            "features": [
                "string"
            ],
            "description": "string",
            "image_url": "string"
        },
        "state": {
            "hp": 0,
            "ap": 0
        },
        "attributes": {
            "dexterity": 0,
            "strength": 0,
            "intelligence": 0,
            "willpower": 0,
            "endurance": 0,
            "perception": 0,
            "social": 0,
            "chance": 0
        }
    }
    return character


@router.patch("/character", response_model=D6Character, tags=["character"])
async def patch_character(character: D6Character):
    """
    PATCH update, character with partial json.
    :param character:
    :return: D6Character
    """
    character = {
        "key": {
            "id": 0,
            "universe": "realms",
            "player": "user@example.com"
        },
        "traits": {
            "name": "string",
            "age": 0,
            "height": "string",
            "weight": 0,
            "species": "string",
            "hair_color": "string",
            "eye_color": "string",
            "origin_of_birth": "string",
            "features": [
                "string"
            ],
            "description": "string",
            "image_url": "string"
        },
        "state": {
            "hp": 0,
            "ap": 0
        },
        "attributes": {
            "dexterity": 0,
            "strength": 0,
            "intelligence": 0,
            "willpower": 0,
            "endurance": 0,
            "perception": 0,
            "social": 0,
            "chance": 0
        }
    }
    return character


@router.post("/character", response_model=D6Character, tags=["character"])
async def post_character(character: D6Character):
    """
    POST create character with full json entry.
    :param character:
    :return:
    """
    character = {
        "key": {
            "id": 0,
            "universe": "realms",
            "player": "user@example.com"
        },
        "traits": {
            "name": "string",
            "age": 0,
            "height": "string",
            "weight": 0,
            "species": "string",
            "hair_color": "string",
            "eye_color": "string",
            "origin_of_birth": "string",
            "features": [
                "string"
            ],
            "description": "string",
            "image_url": "string"
        },
        "state": {
            "hp": 0,
            "ap": 0
        },
        "attributes": {
            "dexterity": 0,
            "strength": 0,
            "intelligence": 0,
            "willpower": 0,
            "endurance": 0,
            "perception": 0,
            "social": 0,
            "chance": 0
        }
    }
    return character


@router.put("/character", response_model=D6Character, tags=["character"])
async def put_character(character: D6Character):
    """
    PUT update, overwrite, character with full json entry.
    :param character:
    :return:
    """
    character = {
        "key": {
            "id": 0,
            "universe": "realms",
            "player": "user@example.com"
        },
        "traits": {
            "name": "string",
            "age": 0,
            "height": "string",
            "weight": 0,
            "species": "string",
            "hair_color": "string",
            "eye_color": "string",
            "origin_of_birth": "string",
            "features": [
                "string"
            ],
            "description": "string",
            "image_url": "string"
        },
        "state": {
            "hp": 0,
            "ap": 0
        },
        "attributes": {
            "dexterity": 0,
            "strength": 0,
            "intelligence": 0,
            "willpower": 0,
            "endurance": 0,
            "perception": 0,
            "social": 0,
            "chance": 0
        }
    }
    return character
