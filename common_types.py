# pyright: strict

from __future__ import annotations
from enum import StrEnum
from typing import Protocol

class SpriteType(StrEnum):
    GROWING = 'growing'
    HARVESTABLE = 'harvestable'

    

class Crop(Protocol):
    _cost: int

    _name: str

    _days_to_grow: int

    _harvest_value:int

    _sprites: dict[SpriteType, str]

    _water_history: list[int]


class SeedPacketMode(Protocol):
    _starting_pesos: int

    _r: int 

    _c: int

    _available_crops: tuple[str,...]

    @property
    def starting_pesos(self) -> int:
        ...
    @property
    def r(self) -> int:
        ...

    @property
    def c(self) -> int:
        ...

    @property
    def available_crops(self) -> tuple[Crop,...]:
        ...

    def crop_create(self, crop: str):
        ...

class WateringCan(Protocol):
    _AOE : int 

    _description : str



