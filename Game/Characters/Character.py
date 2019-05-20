
from Game.Objects import Object

class Character(Object):

    def __init__(self, field, x, y):
        self.field = field
        self.x = x
        self.y = y

        self.field.addObject(x, y, self)

    def getVisibilityPriority(self):
        return 100000;

    def isTransparent(self):
        return True

    def actUp(self):
        return self.act(self.x, self.y, self.x, self.y - 1)

    def actDown(self):
        return self.act(self.x, self.y, self.x, self.y + 1)

    def actLeft(self):
        return self.act(self.x, self.y, self.x - 1, self.y)

    def actRight(self):
        return self.act(self.x, self.y, self.x + 1, self.y)

    def act(self, fromX, fromY, x, y):
        if self.field.canMoveTo(x, y, self):
            self.field.moveTo(self, x, y)
            return True
        elif self.field.canBeInteractedWith(x, y, self):
            self.field.interact(x, y, self)
            return True

        return False
