
from .Object import Object

class Exit(Object):
    def isPassable(self, character):
        return character.hasTarget

    def stepOn(self, player):
        player.exited = True
