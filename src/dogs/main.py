from typing import Annotated, Literal

from msgspec import Struct
from sanic import Sanic, json
from sanic.response import JSONResponse
from sanic_ext import validate

app = Sanic("Dogs")


class Dog(Struct):
    name: str
    breed: str
    age: float


@app.get("/")
@validate(json=Dog)
async def dogs(
    request,
) -> Annotated[JSONResponse, list[dict[Literal["name", "breed", "age"], str | float]]]:
    return json(
        [
            {"name": "Bear", "breed": "bulldog", "age": 10},
            {"name": "Charlie", "breed": "Retriever", "age": 2},
            {"name": "Buddy", "breed": "POODLE", "age": 5.5},
            {"name": "Bella", "breed": "BeagE", "age": 1},
        ],
    )
