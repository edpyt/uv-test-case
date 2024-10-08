import os
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Annotated

from fastapi import Depends, FastAPI
from nicegui import app as nicegui_app
from nicegui import ui


@dataclass
class Config:
    CARS: str = field(default_factory=lambda: os.getenv("CARS_API", default="http://localhost:8001"))
    CATS: str = field(default_factory=lambda: os.getenv("CATS_API", default="http://localhost:8002"))
    DOGS: str = field(default_factory=lambda: os.getenv("DOGS_API", default="http://localhost:8003"))


@lru_cache
def get_config() -> Config:
    return Config()


def frontend_init(fastapi_app: FastAPI):
    @ui.page("/")
    def show(config: Annotated[Config, Depends(get_config)]):
        ui.dark_mode().bind_value(nicegui_app.storage.user, "dark_mode")
        ui.checkbox("dark mode").bind_value(nicegui_app.storage.user, "dark_mode")

        ui.label("UV Test Case!").style("font-size: 18px;")

        with ui.grid():
            ui.link("cars", config.CARS)
            ui.link("cats", config.CATS)
            ui.link("dogs", config.DOGS)

    ui.run_with(fastapi_app, mount_path="/", storage_secret="uv-testte")


app = FastAPI()
frontend_init(app)
