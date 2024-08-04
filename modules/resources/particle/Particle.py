
from ..util.Util import importFolderSprites
from pygame import sprite
class Particle(sprite.Sprite):
    #Class constructor
    def __init__(self, pos: tuple, particle: str):
        super().__init__()
        self._frameIndex = 0
        self._animationSpeed = 0.5
        path: str = ""
        match particle:
            case "jump":
                path = "../../../assets/sprites/particles/dust/jump"
            case "land":
                path = "../../../assets/sprites/particles/dust/land"
        self._frames = importFolderSprites(path)
        self._image = self._frames[self.frameIndex]
        self._rect = self.image.get_rect(center=pos)

    #Getters and setters
    @property
    def frameIndex(self):
        return self._frameIndex

    @frameIndex.setter
    def frameIndex(self, newValue):
        self._frameIndex = newValue

    @property
    def animationSpeed(self):
        return self._animationSpeed

    @animationSpeed.setter
    def animationSpeed(self, newValue):
        self._animationSpeed = newValue

    @property
    def frames(self):
        return self._frames

    @frames.setter
    def frames(self, newValue):
        self._frames = newValue

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

    #Instance methods
    def animate(self):
        #Handles the animation loop
        self.frameIndex += self.animationSpeed
        if self.frameIndex >= len(self.frames):
            self.kill()
        else:
            self.image=self.frames[int(self.frameIndex)]
    def update(self, xShift: int, yShift: int):
        #Events to occur every frame.
        self.animate()
        self.rect.x += xShift
        self.rect.y += yShift
