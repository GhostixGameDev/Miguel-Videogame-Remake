import pygame
from modules.resources.util.Util import scaler
from modules.resources.util.Util import importFolderSprites
from math import sin
from modules.resources.config.ConfigLoader import tileSizeScaled, scale


def importCharacterAssets(path: str):
    animations = {"idle": [], "run": [], "jump": []}
    idleFrames = len(animations["idle"])
    runFrames = len(animations["run"])
    jumpFrames = len(animations["jump"])
    for animation in animations.keys():
        fullPath = path + animation
        animations[animation] = importFolderSprites(fullPath)
    for i in range(idleFrames):
        animations["idle"][i] = scaler(animations["idle"][i], tileSizeScaled, tileSizeScaled)
    for i in range(runFrames):
        animations["run"][i] = scaler(animations["run"][i], tileSizeScaled, tileSizeScaled)
    for i in range(jumpFrames):
        animations["jump"][i] = scaler(animations["jump"][i], tileSizeScaled, tileSizeScaled)
    return animations


def importDustParticles():
    spritesPath = "../assets/sprites/particles/dust/"
    dustParticles = {"run": [], "land": [], "jump": []}
    runFrames = len(dustParticles["run"])
    landFrames = len(dustParticles["land"])
    jumpFrames = len(dustParticles["jump"])
    for animation in dustParticles.keys():
        fullPath = spritesPath + animation
        dustParticles[animation] = importFolderSprites(fullPath)
    for i in range(runFrames):
        dustParticles["run"][i] = scaler(dustParticles["run"][i], tileSizeScaled / 4, tileSizeScaled / 4)
    for i in range(landFrames):
        dustParticles["land"][i] = scaler(dustParticles["land"][i], tileSizeScaled / 4, tileSizeScaled / 4)
    for i in range(jumpFrames):
        dustParticles["jump"][i] = scaler(dustParticles["jump"][i], tileSizeScaled / 4, tileSizeScaled / 4)

    return dustParticles


def waveValue():
    value = sin(pygame.time.get_ticks())
    if value >= 0:
        return 255
    else:
        return 0


class Player(pygame.sprite.Sprite):
    # Class constructor
    def __init__(self, position: list, surface: pygame.surface, path: str, jumpParticles, updatedLives: int):
        super().__init__()
        self._lives = updatedLives
        self._animations = importCharacterAssets(path)
        self._dustParticles = importDustParticles()
        self._dustState = "land"
        self._dustFrameIndex = 0
        self._dustAnimationSpeed = 0.15
        self._frameIndex = 0
        self._jumpParticles = jumpParticles
        self._animationSpeed = 0.15
        self._displaySurface = surface
        self._sprite = self._animations["idle"][self.frameIndex]
        self._rect = self._sprite.get_rect(topleft=position)
        self._direction = pygame.math.Vector2(0, 0)
        self._speed = 4 * scale
        self._gravity = 0.8 * scale
        self._jumpSpeed = -16 * scale
        self._onGround = True
        self._isInvincible = False
        self._invincibilityDuration = 2000
        self._hurtTime = 0
        self._forceMove = False
        self._collisionRect = pygame.Rect(self.rect.topleft, (self.rect.width - 5, self.rect.height))
        # audio
        self._jumpSound = pygame.mixer.Sound("../assets/sounds/jump.ogg")
        # Anim States
        self._animationState = "idle"
        self._facingRight = True

    # Getters and Setters

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, newValue):
        self._lives = newValue

    @property
    def animations(self):
        return self._animations

    @animations.setter
    def animations(self, newValue):
        self._animations = newValue

    @property
    def dustParticles(self):
        return self._dustParticles

    @dustParticles.setter
    def dustParticles(self, newValue):
        self._dustParticles = newValue

    @property
    def dustState(self):
        return self._dustState

    @dustState.setter
    def dustState(self, newValue):
        self._dustState = newValue

    @property
    def dustFrameIndex(self):
        return self._dustFrameIndex

    @dustFrameIndex.setter
    def dustFrameIndex(self, newValue):
        self._dustFrameIndex = newValue

    @property
    def dustAnimationSpeed(self):
        return self._dustAnimationSpeed

    @dustAnimationSpeed.setter
    def dustAnimationSpeed(self, newValue):
        self._dustAnimationSpeed = newValue

    @property
    def frameIndex(self):
        return self._frameIndex

    @frameIndex.setter
    def frameIndex(self, newValue):
        self._frameIndex = newValue

    @property
    def jumpParticles(self):
        return self._jumpParticles

    @jumpParticles.setter
    def jumpParticles(self, newValue):
        self._jumpParticles = newValue

    @property
    def animationSpeed(self):
        return self._animationSpeed

    @animationSpeed.setter
    def animationSpeed(self, newValue):
        self._animationSpeed = newValue

    @property
    def displaySurface(self):
        return self._displaySurface

    @displaySurface.setter
    def displaySurface(self, newValue):
        self._displaySurface = newValue

    @property
    def sprite(self):
        return self._sprite

    @sprite.setter
    def sprite(self, newValue):
        self._sprite = newValue

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, newValue):
        self._rect = newValue

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, newValue):
        self._direction = newValue

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, newValue):
        self._speed = newValue

    @property
    def gravity(self):
        return self._gravity

    @gravity.setter
    def gravity(self, newValue):
        self._gravity = newValue

    @property
    def jumpSpeed(self):
        return self._jumpSpeed

    @jumpSpeed.setter
    def jumpSpeed(self, newValue):
        self._jumpSpeed = newValue

    @property
    def onGround(self):
        return self._onGround

    @onGround.setter
    def onGround(self, newValue):
        self._onGround = newValue

    @property
    def isInvincible(self):
        return self._isInvincible

    @isInvincible.setter
    def isInvincible(self, newValue):
        self._isInvincible = newValue

    @property
    def invincibilityDuration(self):
        return self._invincibilityDuration

    @invincibilityDuration.setter
    def invincibilityDuration(self, newValue):
        self._invincibilityDuration = newValue

    @property
    def hurtTime(self):
        return self._hurtTime

    @hurtTime.setter
    def hurtTime(self, newValue):
        self._hurtTime = newValue

    @property
    def forceMove(self):
        return self._forceMove

    @forceMove.setter
    def forceMove(self, newValue):
        self._forceMove = newValue

    @property
    def collisionRect(self):
        return self._collisionRect

    @collisionRect.setter
    def collisionRect(self, newValue):
        self._collisionRect = newValue

    @property
    def jumpSound(self):
        return self._jumpSound

    @jumpSound.setter
    def jumpSound(self, newValue):
        self._jumpSound = newValue

    @property
    def animationState(self):
        return self._animationState

    @animationState.setter
    def animationState(self, newValue):
        self._animationState = newValue

    @property
    def facingRight(self):
        return self._facingRight

    @facingRight.setter
    def facingRight(self, newValue):
        self._facingRight = newValue

    # Instance methods
    def animateDust(self):
        # Executes the current particle animation.
        animation = self.dustParticles[self.dustState]
        # Makes the run particle animation to the faced direction
        if self.dustState == "run":
            self.dustFrameIndex += self.dustAnimationSpeed
            # loop
            if self.dustFrameIndex >= len(animation):
                self.dustFrameIndex = 0
            # Animation frame
            dustParticle = animation[int(self.dustFrameIndex)]
            # Direction
            if self.facingRight:
                pos = self.rect.bottomleft - pygame.math.Vector2(6, 20)
                self.displaySurface.blit(dustParticle, pos)
            else:
                pos = self.rect.bottomright - pygame.math.Vector2(6, 20)
                self.displaySurface.blit(dustParticle, pos)

    def animate(self):
        #Loads all the frames of the respective animation.
        animation = self.animations[self.animationState]
        # advances one frame
        self.frameIndex += self.animationSpeed
        # loop
        if self.frameIndex >= len(animation):
            self.frameIndex = 0
        # selects the sprite for the respective frame
        frame = animation[int(self.frameIndex)]
        # Applies the sprite whether its facing right or left
        if self.facingRight:
            self.sprite = frame
            self.rect.bottomleft = self.collisionRect.bottomleft
        else:
            self.sprite = pygame.transform.flip(frame, True, False)
            self.rect.bottomright = self.collisionRect.bottomright
        # Animates the lingering of the sprites if it is invincible.
        if self.isInvincible:
            alpha = waveValue()
            self.sprite.set_alpha(alpha)
        else:
            self.sprite.set_alpha(255)
        # Updates the hit box.
        self.rect = self.sprite.get_rect(midbottom=self.rect.midbottom)

    def getInput(self):
        #Checks the user keyboard input and makes the respective action per each key.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction.x = 1
            self.facingRight = True
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.facingRight = False
        elif not self.forceMove:
            self.direction.x = 0
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            if self.onGround:
                self.jumpParticles(self.rect.midbottom)
            self.jump()

    def getStatus(self):
        if self.direction.y != 0:
            self.animationState = "jump"
            self.dustState = "jump"
        elif self.direction.x != 0:
            self.animationState = "run"
            self.dustState = "run"
        else:
            self.animationState = "idle"
            self.dustState = "land"

    def applyGravity(self):
        #Constantly applies the gravity, dragging the character down at the speed of gravity.
        self.direction.y += self.gravity
        self.collisionRect.y += self.direction.y

    def jump(self):
        #If not in the air it applies the jump speed, plays the jump sound and sets onGround to false.
        if self.onGround:
            self.jumpSound.play()
            self.direction.y = self.jumpSpeed
            self.onGround = False

    def getDamage(self):
        #Just discounts one life and starts invincibility time.
        if not self.isInvincible:
            self.lives = -1
            self.isInvincible = True
            self.hurtTime = pygame.time.get_ticks()

    def invincibilityTimer(self):
        #Handles the invincibility timer, disables it when time runs out.
        if self.isInvincible:
            currentTime = pygame.time.get_ticks()
            if currentTime - self.hurtTime >= self.invincibilityDuration:
                self.isInvincible = False

    def update(self):
        #Handles all the events that have to occur on every frame.
        self.getInput()
        self.getStatus()
        self.animate()
        self.animateDust()
        self.invincibilityTimer()
