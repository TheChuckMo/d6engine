from fastapi import APIRouter

router = APIRouter()


@router.get("/dice", tags=["dice"])
async def read_dice():
    return [{"1d6": 4}, {"1d6": 2}]
