from pygame import sprite, Surface
from modules.resources.config.ConfigLoader import tileSizeScaled
class Tile(sprite.Sprite):
    def __init__(self, size: int, x: int, y: int):
        super().__init__()
        self.image = Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, xShift: float, yShift: float):
        self.rect.x += xShift
        self.rect.y += yShift
