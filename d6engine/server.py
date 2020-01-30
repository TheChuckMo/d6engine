from fastapi import Depends, FastAPI, Header, HTTPException
from starlette.staticfiles import StaticFiles

from .routers import character, dice

app = FastAPI()

app.include_router(character.router)
app.include_router(dice.router)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return {"message": "Hello World"}

