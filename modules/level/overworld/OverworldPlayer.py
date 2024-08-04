from pygame import sprite, Rect, image, BLEND_RGBA_MULT

from modules.resources.util.Util import scaler


class Node(sprite.Sprite):
    def __init__(self, position: tuple, status: bool, playerSpeed: float, path: str):
        super().__init__()
        self.path = path
        self.image = scaler(image.load(self.path), 150, 130)
        if status:
            self.status = True
        else:
            self.status = False
        self.rect = self.image.get_rect(center=position)
        self.checkPoint = Rect(self.rect.centerx - (playerSpeed / 2), self.rect.centery - playerSpeed, playerSpeed,
                               playerSpeed)

    def update(self):
        if self.status:
            self.image = scaler(image.load(self.path), 150, 130).convert_alpha()
        else:
            tintedSurface = self.image.copy()
            tintedSurface.fill("black", None, BLEND_RGBA_MULT)
            self.image.blit(tintedSurface, (0, 0))
