from pydantic import BaseModel, field_validator
from quart import Quart

app = Quart(__name__)


class Cat(BaseModel):
    name: str
    age: float

    @field_validator("name")
    def name_title(cls, name: str) -> str:
        return name.title()


@app.get("/")
async def cats() -> list[dict]:
    return list(
        map(
            lambda cat: cat.model_dump(),
            map(
                Cat.model_validate,
                (
                    {"name": "pushok", "age": 1},
                    {"name": "MartiK", "age": 3},
                    {"name": "MaxWELL", "age": 0},
                ),
            ),
        )
    )


if __name__ == "__main":
    app.run()
