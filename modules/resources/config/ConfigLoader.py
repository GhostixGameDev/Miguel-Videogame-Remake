# ================================
import configparser
import os
# CONFIGURATION
config = configparser.ConfigParser()
homeDir = os.path.expanduser("~")
gamePath = homeDir + "\\AppData\\Roaming\\Skibidi Miguel Bizarre Adventure\\config\\gameConfig.ini"

#Reads or creates the config file depends on whether it exists.
try:
    # Creates config file if doesnt exist.
    gameConfig = open(gamePath, "x")
    gameConfig.close()
    with open(gamePath, "w") as gameConfig:
        gameConfig.write("""
[GAME_CONFIG]\n
firsttime = true\n
screenwidth = 1366\n
screenheight = 768\n
fullscreen = false\n
language = es_ES\n
maxfps = 60""")
except FileExistsError:
    pass
finally:
    config.read(gamePath)
    firstTime: bool = config.getboolean("GAME_CONFIG", "firstTime")
    width: int = config.getint("GAME_CONFIG", "screenWidth")
    height: int = config.getint("GAME_CONFIG", "screenHeight")
    fullscreen: bool = config.getboolean("GAME_CONFIG", "fullscreen")
    language: str = config.get("GAME_CONFIG", "language")
    maxFPS: int = config.getint("GAME_CONFIG", "maxFPS")

    # Default values for tiles.
    tileSize = 64
    scale = 1
    tileSizeScaled = tileSize


# Resolution changes.
def updateResolution(newWidth: int, newHeight: int):
    global width
    global height
    global scale
    global tileSize
    global tileSizeScaled
    if firstTime:
        from modules.resources.util.Util import mainMonitorSize
        width = mainMonitorSize()[0]
        height = mainMonitorSize()[1]
        scale = mainMonitorSize()[0] / 1366
    else:
        width = newWidth
        height = newHeight
        scale = newWidth / 1366
    config.set("GAME_CONFIG", "screenWidth", str(width))
    config.set("GAME_CONFIG", "screenHeight", str(height))
    with open(gamePath, 'w') as configfile:
        config.write(configfile)
    tileSizeScaled = round(tileSize * scale)


# Code to execute on import.
updateResolution(width, height)

if __name__ == "__main__":
    print(f"First time? : {firstTime}")
    print(f"Width: {width}, Height: {height}")
    print(f"full screen enabled? : {fullscreen}")
    print(f"Tile Size: {tileSizeScaled}")
