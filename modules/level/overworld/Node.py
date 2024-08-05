from pygame import sprite, Rect, image, BLEND_RGBA_MULT

from modules.resources.util.Util import scaler


class Node(sprite.Sprite):
    # Class constructor
    def __init__(self, position: list, status: bool, playerSpeed: float, path: str):
        super().__init__()
        self._path = path
        self._image = scaler(image.load(self._path), 150, 130)
        if status:
            self._status = True
        else:
            self._status = False
        self._rect = self._image.get_rect(center=position)
        self._hitBox = Rect(self._rect.centerx - (playerSpeed / 2), self._rect.centery - playerSpeed, playerSpeed,
                            playerSpeed)

    # Getters and setters
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, newValue):
        self._path = newValue

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, newValue):
        self._image = newValue

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, newValue):
        self._status = newValue

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, newValue):
        self._rect = newValue

    @property
    def hitBox(self):
        return self._hitBox

    @hitBox.setter
    def hitBox(self, newValue):
        self._hitBox = newValue

    # Instance methods
    def update(self):
        #Every event that runs in each frame.
        if self.status:
            self.image = scaler(image.load(self.path), 150, 130).convert_alpha()
        else:
            #If not unlocked it shows painted black
            tintedSurface = self.image.copy()
            tintedSurface.fill("black", None, BLEND_RGBA_MULT)
            self.image.blit(tintedSurface, (0, 0))
