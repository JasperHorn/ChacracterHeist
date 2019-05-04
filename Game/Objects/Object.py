
class Object:
    def setField(self, field):
        self.field = field

    def isPassable(self, player):
        return True

    def stepOn(self, player):
        pass

    def view(self):
        pass

    def getVisibilityPriority(self):
        return 0

    def isTransparent(self):
        return False

    def canBeInteractedWith(self, character):
        return False

    def interact(self, character):
        pass
