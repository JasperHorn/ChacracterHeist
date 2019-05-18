
from .Object import Object

class Guard(Object):
    def stepOn(self, player):
        player.capture()

    def getVisibilityPriority(self):
        return 100010
