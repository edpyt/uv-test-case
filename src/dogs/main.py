from typing import Literal

from msgspec import Struct
from msgspec.json import decode, encode
from msgspec.structs import asdict
from sanic import Request, Sanic, json
from sanic.response import JSONResponse
from sanic_ext import serializer

app = Sanic("Dogs")


class Dog(Struct, rename="lower"):
    name: str
    breed: str
    age: float

    def __post_init__(self) -> None:
        self.name = self.name.title()
        self.breed = self.breed.lower()


def serialize_dogs(retval, *_, **__) -> JSONResponse:
    dogs: list[Dog] = decode(encode(retval), type=list[Dog])
    return json([asdict(dog) for dog in dogs])


@app.get("/")
@serializer(serialize_dogs)
async def dogs(_: Request) -> list[dict[Literal["name", "breed", "age"], str | float]]:
    return [
        {"name": "Bear", "breed": "bulldog", "age": 10},
        {"name": "Charlie", "breed": "Retriever", "age": 2},
        {"name": "Buddy", "breed": "POODLE", "age": 5.5},
        {"name": "Bella", "breed": "BeagE", "age": 1},
    ]
