from pygame import font, time
from random import random
class JoJoParticle(font.Font):
    #Class constructor
    def __init__(self, fontPath: str, size: int, surface):
        super().__init__(fontPath, size)
        self._x = 0
        self._y = 0
        self._surface =surface
        self._jojoOutline = font.Font(fontPath, size+1)
        self._timePast = 0
        self._xShake = 0
        self._yShake = 0

    #Getters and setters.
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, newValue):
        self._x = newValue

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, newValue):
        self._y = newValue

    @property
    def surface(self):
        return self._surface

    @surface.setter
    def surface(self, newValue):
        self._surface = newValue

    @property
    def jojoOutline(self):
        return self._jojoOutline

    @jojoOutline.setter
    def jojoOutline(self, newValue):
        self._jojoOutline = newValue

    @property
    def timePast(self):
        return self._timePast

    @timePast.setter
    def timePast(self, newValue):
        self._timePast = newValue

    @property
    def xShake(self):
        return self._xShake

    @xShake.setter
    def xShake(self, newValue):
        self._xShake = newValue

    @property
    def yShake(self):
        return self._yShake

    @yShake.setter
    def yShake(self, newValue):
        self._yShake = newValue

    #Instance methods
    def _shake_(self):
        #Makes the letters shake like in the series.
        self.xShake = random() * 2.5
        self.xShake -= random() * 1.5
        self.yShake += random() * 2.5
        self.yShake = random() * 1.5
    def draw(self, text, color, x, y):
        #Draws the letters with an outline and moves them accordingly to the shaking.
        self.x = x + self.xShake
        self.y = y + self.yShake
        jojoOutlineRender = self.jojoOutline.render(text, False, (67, 35, 88))
        jojo = self.render(text, False, color).convert_alpha()
        self.surface.blit(jojo, (self.x, self.y))
        self.surface.blit(jojoOutlineRender, (self.x, self.y))

    def textTimer(self):
        #Handles how long the letters appear in screen.
        currentTime = time.get_ticks()
        if currentTime-self.timePast>=2000:
            return True
    def update(self, xShift, yShift):
        #Events that have to run every frame.
        self.x += xShift
        self.y += yShift
        self._shake_()
