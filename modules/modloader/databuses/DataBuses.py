from modules.npc.enemy import Enemy
from modules.player.Player import Player
from modules.resources.particle import Particle
from modules.resources.particle.custom import JoJoParticle
from modules.resources.tiles.StaticTile import StaticTile
from modules.resources.tiles.AnimatedTile import AnimatedTile
from modules.resources.tiles.custom.static.LuckyBlock import LuckyBlock
from modules.resources.tiles.custom.animated.Coin import Coin
from dataclasses import dataclass

#This class manages the buses for the mod loader to load all the custom content.
@dataclass(order=True)
class DataBuses:
    def __init__(self):
        self.__GameTiles = {"vanilla:static": StaticTile, "vanilla:animated": AnimatedTile, "vanilla:lucky_block": LuckyBlock, "vanilla:coin": Coin}
        self.__GameEnemies = {"vanilla:generic": Enemy}
        self.__GameParticles = {"vanilla:generic": Particle, "vanilla:jojo_particle": JoJoParticle}
        self.__PlayerController = {"player": Player}
    #Getters and setters.
    @property
    def GameTiles(self):
        return self.__GameTiles
    @property
    def GameEnemies(self):
        return self.__GameEnemies
    @property
    def GameParticles(self):
        return self.__GameParticles
    @property
    def PlayerController(self):
        return self.__PlayerController
    #Instance methods
    def addTiles(self, modID: str, name: str, newTile):
        self.GameTiles.update({modID + name: newTile})
    def addEnemies(self, modID: str, name: str, newEnemy):
        self.GameEnemies.append(newEnemy)
    def addParticles(self, modID: str, name: str, newParticle):
        self.GameParticles.append(newParticle)
    def addPlayerController(self, modID: str, name: str, newPlayerController):
        self.PlayerController.append(newPlayerController)

