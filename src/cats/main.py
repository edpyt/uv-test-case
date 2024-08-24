from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Cat(BaseModel):
    name: str
    age: int


@app.get("/", response_model=list[Cat])
def cats() -> list[dict[Literal["name", "age"], str | int]]:
    return [
        {"name": "Pushok", "age": 1},
        {"name": "Martik", "age": 3},
        {"name": "Maxwell", "age": 0},
    ]
