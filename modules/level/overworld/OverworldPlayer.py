from pygame import sprite, image


class OverworldPlayer(sprite.Sprite):
    # Class constructor
    def __init__(self, position: list, player: str):
        super().__init__()
        self._position = position
        self._image = image.load(player).convert_alpha()
        self._rect = self._image.get_rect(center=position)

    # Getters and setters
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, newValue):
        self._position = newValue

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, newValue):
        self._image = newValue

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, newValue):
        self._rect = newValue

    # Instance methods
    def update(self):
        # Events that run on each frame.
        self.rect.center = self.position
