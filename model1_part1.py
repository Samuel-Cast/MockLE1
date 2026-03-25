from common_types import SeedPacketMode, Crop, SpriteType, WateringCan

class Turnip:
    def __init__(self) -> None:
        self._cost = 300

        self._name = "turnip"

        self._days_to_grow = 2

        self._harvest_value = 500

        self._sprites = {SpriteType.GROWING : "t",
        SpriteType.HARVESTABLE: "T"}

        self._water_history = []

    

class AnimalCrossingMode:
    def __init__(self) -> None:
        self._starting_pesos = 1000

        self._r = 5

        self._c = 5

        self._available_crops: tuple[str,...]= tuple("turnip")

        self._water_history = []

        self._convo 
    @property
    def starting_pesos(self) -> int:
        ...
    @property
    def r(self) -> int:
        ...

    @property
    def c(self) -> int:
        ...
    def crop_create(self, crop: str):
        match crop:
            case "turnip":
                return Turnip()
            case _:
                raise ValueError()






class Model():
    
    def __init__(self,  packet: SeedPacketMode, cans: tuple[WateringCan,...] ) -> None:
        self._day = 1

        self._packet = packet

        self._cans = cans

        self._grid = [[None,] * packet.c] * packet.r

        self._pesos =  packet.starting_pesos
    def plant(self, crop:Crop,i: int, j: int):

        new_crop = self._packet.crop_create()

        self._grid[i] = self._grid[i][:j] + new_crop + self._grid[i][j+1:]

        return True




        



        
        

