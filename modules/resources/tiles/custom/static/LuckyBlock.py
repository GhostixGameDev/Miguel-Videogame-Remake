from modules.resources.tiles.StaticTile import StaticTile, image
class LuckyBlock(StaticTile):
    def __init__(self, size: int, x: int, y: int, path: str, state: bool):
        super().__init__(size, x, y, image.load(path).convert_alpha())
        self.state = state
    def updateState(self, state: bool):
        self.state = state

