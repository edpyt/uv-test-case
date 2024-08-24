from dataclasses import dataclass

from fastapi import FastAPI

app = FastAPI()


@dataclass
class Car:
    mark: str


@app.get("/", response_model=list[Car])
def cars() -> list[str]:
    return ["Lada", "Chevrolette", "Daewoo", "Mazda"]
