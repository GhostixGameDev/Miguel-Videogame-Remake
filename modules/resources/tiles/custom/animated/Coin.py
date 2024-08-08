from modules.resources.tiles.AnimatedTile import AnimatedTile

class Coin(AnimatedTile):
    def __init__(self, size: int, x: int, y: int, path: str, value: int):
        super().__init__(size, x, y, path)
        centerX = x + int(size/2)
        centerY = y + int(size/2)
        self.rect = self.image.get_rect(center=(centerX, centerY))
        self.value = value

