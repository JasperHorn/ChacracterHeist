
from .Object import Object

class TargetTreasure(Object):
    def stepOn(self, player):
        player.setHasTarget(True)
        self.field.removeObject(self)
