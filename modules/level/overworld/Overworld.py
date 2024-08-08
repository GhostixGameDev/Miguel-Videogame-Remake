
import pygame

from modules.level.overworld.Node import Node
from modules.level.overworld.OverworldPlayer import OverworldPlayer
from modules.level.Levels import overworldInfo


class Overworld:
    def __init__(self, startLevel: int, maxLevel: int, screen: pygame.display, createLevel):

        #Setup
        self._player = pygame.sprite.GroupSingle()
        self._displaySurface = screen
        self._maxLevel = maxLevel
        self._currentLevel = startLevel
        self._createLevel = createLevel
        self._nodes = pygame.sprite.Group()

        #Player things
        self._moveDirection = pygame.math.Vector2(0, 0)
        self._speed = 12
        self._moving = False
        #Assets
        self.setupNodes()
        self.setupPlayer()

        #timers
        self._startTime = pygame.time.get_ticks()
        self._allowInput=True
        self._timerLength=500

    #Getters and setters
    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, newValue):
        self._player = newValue

    @property
    def displaySurface(self):
        return self._displaySurface

    @displaySurface.setter
    def displaySurface(self, newValue):
        self._displaySurface = newValue

    @property
    def maxLevel(self):
        return self._maxLevel

    @maxLevel.setter
    def maxLevel(self, newValue):
        self._maxLevel = newValue

    @property
    def currentLevel(self):
        return self._currentLevel

    @currentLevel.setter
    def currentLevel(self, newValue):
        self._currentLevel = newValue

    @property
    def createLevel(self):
        return self._createLevel

    @createLevel.setter
    def createLevel(self, newValue):
        self._createLevel = newValue

    @property
    def nodes(self):
        return self._nodes

    @nodes.setter
    def nodes(self, newValue):
        self._nodes = newValue

    @property
    def moveDirection(self):
        return self._moveDirection

    @moveDirection.setter
    def moveDirection(self, newValue):
        self._moveDirection = newValue

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, newValue):
        self._speed = newValue

    @property
    def moving(self):
        return self._moving

    @moving.setter
    def moving(self, newValue):
        self._moving = newValue

    @property
    def startTime(self):
        return self._startTime

    @startTime.setter
    def startTime(self, newValue):
        self._startTime = newValue

    @property
    def allowInput(self):
        return self._allowInput

    @allowInput.setter
    def allowInput(self, newValue):
        self._allowInput = newValue

    @property
    def timerLength(self):
        return self._timerLength

    @timerLength.setter
    def timerLength(self, newValue):
        self._timerLength = newValue



    #Instance methods
    def setupNodes(self):
        # Creates the levels in the menu
        for index, nodeData in enumerate(overworldInfo.values()):
            if index <= self.maxLevel:
                nodeSprite = Node(nodeData["nodePos"], True, self.speed, nodeData["nodeAssets"])
            else:
                nodeSprite = Node(nodeData["nodePos"], False, self.speed, nodeData["nodeAssets"])
            self.nodes.add(nodeSprite)
    def setupPlayer(self):
        #Creates the player.
        playerSprite = OverworldPlayer(self.nodes.sprites()[self.currentLevel].rect.center)
        self.player.add(playerSprite)
    def drawLines(self):
        #Draws the path between unlocked levels
        points=[]
        points=[node["nodePos"] for index,node in enumerate(overworldInfo.values()) if index<=self.maxLevel]
        if len(points) > 0:
            try:
                pygame.draw.lines(self.displaySurface, "red", False, points, 6)
            finally:
                pass
    def input(self):
        #Checks for the keyboard input and executes the appropriate action.
        key = pygame.key.get_pressed()
        if not self.moving and self.allowInput:
            if key[pygame.K_d] and self.currentLevel !=self.maxLevel:
                self.moveDirection = self.getMovementData(1)
                self.currentLevel += 1
                self.moving=True
            elif key[pygame.K_a] and self.currentLevel !=0:
                self.moveDirection = self.getMovementData(-1)
                self.currentLevel -= 1
                self.moving=True
            elif key[pygame.K_SPACE]:
                self.createLevel(self.currentLevel)
    def getMovementData(self, direction):
        #Calculates the movement for the player to reach the objective
        start = pygame.math.Vector2(self.nodes.sprites()[self.currentLevel].rect.center)
        end = pygame.math.Vector2(self.nodes.sprites()[self.currentLevel+(1*direction)].rect.center)
        return (end - start).normalize()
    def updatePlayerPos(self):
        #Moves the player
        if self.moving and self.moveDirection:
            self.player.sprite.pos += self.moveDirection * self.speed
            targetNode = self.nodes.sprites()[self.currentLevel]
            if targetNode.checkPoint.collidepoint(self.player.sprite.pos):
                self.moving = False
                self.moveDirection = pygame.math.Vector2(0, 0)
    def inputTimer(self):
        #Delay between keyboard inputs
        if not self.allowInput:
            currentTime = pygame.time.get_ticks()
            if currentTime - self.startTime >= self.timerLength:
                self.allowInput = True
    def run(self):
        #Events that happen every frame.
        self.displaySurface.fill("#008c96")
        self.input()
        self.nodes.update()
        self.player.update()
        self.updatePlayerPos()
        self.drawLines()
        self.inputTimer()
        self.nodes.draw(self.displaySurface)
        self.player.draw(self.displaySurface)

