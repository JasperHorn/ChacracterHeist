
from .Object import Object

class FogOfWar(Object):
    def getVisibilityPriority(self):
        return 1000000

    def view(self):
        self.field.removeObject(self)
