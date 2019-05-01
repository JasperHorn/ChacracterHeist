
from .Object import Object

class Wall(Object):
    def isPassable(self, character):
        return False
