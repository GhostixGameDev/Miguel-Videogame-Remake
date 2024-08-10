from modules.resources.tiles.Tile import *
from modules.resources.util.Util import scaler
from pygame import image
class StaticTile(Tile):
    def __init__(self, size: int, x: int, y: int, surface: Surface):
        super().__init__(size, x, y)
        self.image = scaler(surface, tileSizeScaled, tileSizeScaled)


