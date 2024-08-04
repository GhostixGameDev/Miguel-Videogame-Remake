from pygame import image
from pygame import transform
from pygame import Surface
from pygame import SRCALPHA
from pygame import Rect
from screeninfo import get_monitors
from os import walk
from csv import reader


# from LevelEditor import tileSize

def scaler(element: image, x: int, y: int):
    return transform.scale(element, (x, y))


def scaleList(elements: list, x: int, y: int):
    amount = len(elements)
    for i in range(amount):
        elements[i] = scaler(elements[i], x, y)
    # We return all the scaled images.
    return elements


def mainMonitorSize():
    size = [0, 0]
    monitors = get_monitors()
    primary = monitors[0]
    if len(monitors) > 1:
        for monitor in monitors:
            if monitor.is_primary:
                primary = monitor
    size[0] = primary.width
    size[1] = primary.height
    # We check for the main monitor and return its size.
    return size


# This function walks all the folder passed in the path argument and return the loaded sprites from it.
def importFolderSprites(path: str):
    spritesheet = []
    for _, __, names in walk(path):
        for sprite in names:
            fullpath = path + "/" + sprite
            loadedSprite = image.load(fullpath).convert_alpha()
            spritesheet.append(loadedSprite)
    return spritesheet


def importCsvLayout(path: str):
    terrainMap = []
    # We fill a 2D Array with all the map layout info.
    with open(path) as layout:
        level = reader(layout, delimiter=',')
        for row in level:
            terrainMap.append(list(row))
        return terrainMap


def importCutSpritesheet(path: str):
    from modules.resources.config.ConfigLoader import tileSize
    surface = image.load(path).convert_alpha()
    tileNumX = int(surface.get_size()[0] / tileSize)
    tileNumY = int(surface.get_size()[1] / tileSize)
    cutTiles = []
    for row in range(tileNumY):
        for col in range(tileNumX):
            x = col * tileSize
            y = row * tileSize
            newSurface = Surface((tileSize, tileSize), flags=SRCALPHA)
            newSurface.blit(surface, (0, 0), Rect(x, y, tileSize, tileSize))
            cutTiles.append(newSurface)
    return cutTiles
