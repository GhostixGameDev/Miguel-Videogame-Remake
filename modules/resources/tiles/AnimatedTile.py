from modules.resources.tiles.Tile import *
from modules.resources.util.Util import scaleList, importFolderSprites
class AnimatedTile(Tile):
    def __init__(self, size: int, x: int, y: int, path: str):
        super().__init__(size, x, y)
        self.frames = importFolderSprites(path)
        self.frames = scaleList(self.frames, tileSizeScaled, tileSizeScaled)
        self.frameIndex = 0
        self.image = self.frames[self.frameIndex]
    def animate(self):
        self.frameIndex += 0.15
        if self.frameIndex >= len(self.frames):
            self.frameIndex = 0
        self.image = self.frames[int(self.frameIndex)]

    def update(self, xShift: float, yShift: float):
        self.animate()
        self.rect.x += xShift
        self.rect.y += yShift

