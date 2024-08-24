from dataclasses import dataclass
from typing import Literal

from fastapi import FastAPI

app = FastAPI()


@dataclass
class Car:
    mark: str
    model: str

    def __post_init__(self) -> None:
        self.mark, self.model = map(str.title, (self.mark, self.model))


@app.get("/", response_model=list[Car])
def cars() -> list[dict[Literal["mark", "model"], str]]:
    return [
        {"mark": "LaDa", "model": "PrIoRa"},
        {"mark": "ChevroleTTe", "model": "lacetti"},
        {"mark": "Daewoo", "model": "NeXiA"},
        {"mark": "MaZDa", "model": "rx-7"},
    ]
