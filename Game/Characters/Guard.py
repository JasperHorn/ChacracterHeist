
from .Character import Character

class Guard(Character):
    def stepOn(self, player):
        player.capture()

    def getVisibilityPriority(self):
        return 100010
