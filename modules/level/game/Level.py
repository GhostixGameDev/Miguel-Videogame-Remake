import pygame

from modules.level.Levels import levels
from modules.resources.config.ConfigLoader import tileSizeScaled
from modules.resources.util.Util import importCsvLayout, importCutSpritesheet
from modules.modloader.databuses.DataBuses import DataBuses
from modules.level.overworld.Overworld import Overworld

class Level:
    def __init__(self, currentLevel, surface, createOverworld, updateCoins, coins, lives, createLevel):
        #Level setup
        self.__displaySurface: pygame.display = surface
        self.__worldShiftX: float = 0
        self.__worldShiftY: float = 0
        self.__currentLevel = currentLevel
        self.__updateCoins = updateCoins
        levelMeta = levels[currentLevel]
        levelData = levelMeta["content"]
        self.__newMaxLevel = levelMeta["unlock"]
        self.__createOverworld = createOverworld
        self.__createLevel = createLevel
        self.__initScrolled: bool = True
        #Mod loader
        self.__data = DataBuses()
        #Player
        playerLayout = importCsvLayout(levelData["constraints3"])
        self.__player = pygame.sprite.GroupSingle()
        self.__goal = pygame.sprite.GroupSingle()
        self.__coins = coins
        self.__updateLives = lives
        self.__playerSetup(playerLayout)
        self.__playerOnGround = False

        #Particles
        self.__JoJoText = self.data.GameParticles["vanilla:jojo_particle"]("../assets/fonts/SF Fedora.ttf", 20, self.displaySurface)
        self.__JoJoTextOverlain = self.data.GameParticles["vanilla:jojo_particle"]("../assets/fonts/SF Fedora.ttf", 20, self.displaySurface)
        self.__stopJojo = True
        self.__dustSprite = pygame.sprite.GroupSingle()

        #Audio
        self.__coinSound = pygame.mixer.Sound("../assets/sounds/coin.ogg")

        #Layouts
        boxesLayout = importCsvLayout(levelData["boxes"])
        backgroundLayout = importCsvLayout(levelData["background"])
        coinsLayout = importCsvLayout(levelData["coins"])
        enemiesLayout = importCsvLayout(levelData["enemies"])
        LuckyBlocksLayout = importCsvLayout(levelData["lucky_blocks"])
        decorationLayout = importCsvLayout(levelData["decoration"])
        #Background
        self.__backgroundSprites = self._createTileGroup_(backgroundLayout, "background")
        #boxes
        self.__boxesSprites = self._createTileGroup_(boxesLayout, "boxes")
        #coins
        self.__coinsSprites = self._createTileGroup_(coinsLayout, "coins")
        #Enemies
        self.__EnemySprites = self._createTileGroup_(enemiesLayout, "enemies")
        self.__luckyBlocksSprites = self._createTileGroup_(LuckyBlocksLayout, "lucky_blocks")
        #Decoration
        self.__decorationSprites = self._createTileGroup_(decorationLayout, "decoration")

        #Constraints
        constraintLayout = importCsvLayout(levelData["constraints"])
        self.__constraintSprites = self._createTileGroup_(constraintLayout, "constraints")
        constraintLayout2 = importCsvLayout(levelData["constraints2"])
        self.__constraintSprites2 = self._createTileGroup_(constraintLayout2, "constraints2")

    #Getters and setters
    @property
    def displaySurface(self):
        return self.__displaySurface

    @property
    def worldShiftX(self):
        return self.__worldShiftX

    @worldShiftX.setter
    def worldShiftX(self, newValue):
        self.__worldShiftX = newValue

    @property
    def worldShiftY(self):
        return self.__worldShiftY

    @worldShiftY.setter
    def worldShiftY(self, newValue):
        self.__worldShiftY = newValue

    @property
    def currentLevel(self):
        return self.__currentLevel


    @property
    def updateCoins(self):
        return self.__updateCoins

    @updateCoins.setter
    def updateCoins(self, newValue):
        self.__updateCoins = newValue

    @property
    def newMaxLevel(self):
        return self.__newMaxLevel

    @newMaxLevel.setter
    def newMaxLevel(self, newValue):
        self.__newMaxLevel = newValue

    @property
    def createOverworld(self):
        return self.__createOverworld


    @property
    def createLevel(self):
        return self.__createLevel


    @property
    def initScrolled(self):
        return self.__initScrolled

    @initScrolled.setter
    def initScrolled(self, newValue):
        self.__initScrolled = newValue

    @property
    def data(self):
        return self.__data


    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, newValue):
        self.__player = newValue

    @property
    def goal(self):
        return self.__goal

    @goal.setter
    def goal(self, newValue):
        self.__goal = newValue

    @property
    def coins(self):
        return self.__coins

    @coins.setter
    def coins(self, newValue):
        self.__coins = newValue

    @property
    def updateLives(self):
        return self.__updateLives

    @updateLives.setter
    def updateLives(self, newValue):
        self.__updateLives = newValue

    @property
    def playerOnGround(self):
        return self.__playerOnGround

    @playerOnGround.setter
    def playerOnGround(self, newValue):
        self.__playerOnGround = newValue

    @property
    def JoJoText(self):
        return self.__JoJoText

    @JoJoText.setter
    def JoJoText(self, newValue):
        self.__JoJoText = newValue

    @property
    def JoJoTextOverlain(self):
        return self.__JoJoTextOverlain

    @JoJoTextOverlain.setter
    def JoJoText2(self, newValue):
        self.__JoJoTextOverlain = newValue

    @property
    def stopJojo(self):
        return self.__stopJojo

    @stopJojo.setter
    def stopJojo(self, newValue):
        self.__stopJojo = newValue

    @property
    def dustSprite(self):
        return self.__dustSprite

    @dustSprite.setter
    def dustSprite(self, newValue):
        self.__dustSprite = newValue

    @property
    def coinSound(self):
        return self.__coinSound

    @coinSound.setter
    def coinSound(self, newValue):
        self.__coinSound = newValue

    @property
    def backgroundSprites(self):
        return self.__backgroundSprites

    @backgroundSprites.setter
    def backgroundSprites(self, newValue):
        self.__backgroundSprites = newValue

    @property
    def boxesSprites(self):
        return self.__boxesSprites

    @boxesSprites.setter
    def boxesSprites(self, newValue):
        self.__boxesSprites = newValue

    @property
    def coinsSprites(self):
        return self.__coinsSprites

    @coinsSprites.setter
    def coinsSprites(self, newValue):
        self.__coinsSprites = newValue

    @property
    def EnemySprites(self):
        return self.__EnemySprites

    @EnemySprites.setter
    def EnemySprites(self, newValue):
        self.__EnemySprites = newValue

    @property
    def luckyBlocksSprites(self):
        return self.__luckyBlocksSprites

    @luckyBlocksSprites.setter
    def luckyBlocksSprites(self, newValue):
        self.__luckyBlocksSprites = newValue

    @property
    def decorationSprites(self):
        return self.__decorationSprites

    @decorationSprites.setter
    def decorationSprites(self, newValue):
        self.__decorationSprites = newValue

    @property
    def constraintSprites(self):
        return self.__constraintSprites

    @constraintSprites.setter
    def constraintSprites(self, newValue):
        self.__constraintSprites = newValue

    @property
    def constraintSprites2(self):
        return self.__constraintSprites2

    @constraintSprites2.setter
    def constraintSprites2(self, newValue):
        self.__constraintSprites2 = newValue
    #Instance methods
    def _input_(self):
        key=pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            self.createOverworld(self.currentLevel, 0)
    def _createTileGroup_(self, layout, tileType):
        spriteGroup = pygame.sprite.Group()
        for rowIndex, row in enumerate(layout):
            for colIndex, col in enumerate(row):
                if col != "-1":
                    x = colIndex * tileSizeScaled
                    y = rowIndex * tileSizeScaled
                    match tileType:
                        case "boxes":
                            sprite = self.data.GameTiles["vanilla:static"](tileSizeScaled, x, y, pygame.image.load("../../../assets/sprites/object/box.png").convert_alpha())
                        case "background":
                            backgroundTileList = importCutSpritesheet("../../../assets/sprites/background/tiles/backgroundTiles.png")
                            tileSurface = backgroundTileList[int(col)]
                            sprite = self.data.GameTiles["vanilla:static"](tileSizeScaled, x, y, tileSurface)
                        case "coins":
                            coinPath = ""
                            value = 0
                            if col == "0":
                                coinPath = "../../../assets/sprites/objects/coins/gold"
                                value = 5
                            else:
                                coinPath = "../../../assets/sprites/objects/coins/silver"
                                value = 1
                            sprite = self.data.GameTiles["vanilla:coin"](tileSizeScaled, x, y, coinPath, value)
                        case "decoration":
                            decoTileList = importCutSpritesheet("../../../assets/sprites/background/tiles/backgroundTiles.png")
                            tileSurface = decoTileList[int(col)]
                            sprite = self.data.GameTiles["vanilla:static"](tileSizeScaled, x, y, tileSurface)
                        case "enemies":
                            sprite = self.data.GameEnemies["vanilla:generic"](tileSizeScaled, x, y)
                        case "constraints":
                            sprite = self.data.GameTiles["vanilla:generic"](tileSizeScaled, x, y)
                        case "constraints2":
                            sprite = self.data.GameTiles["vanilla:generic"](tileSizeScaled, x, y)
                        case "lucky_blocks":
                            if col == "1":
                                blockPath = "../../../assets/sprites/objects/luckyblock/sliced/luckyBlock02.png"
                                state = False
                            else:
                                blockPath = "../../../assets/sprites/objects/luckyblock/sliced/luckyBlock01.png"
                                state = True
                            sprite = self.data.GameTiles["vanilla:lucky_block"](tileSizeScaled, x, y, blockPath, state)
                    spriteGroup.add(sprite)
        return spriteGroup



