
from .Objects import Object

class PlayerCharacter(Object):

    def __init__(self, field, x, y):
        self.field = field
        self.x = x
        self.y = y
        self.observers = []
        self.money = 0
        self.hasTarget = False
        self.exited = False

        self.field.addObject(x, y, self)

    def getVisibilityPriority(self):
        return 100000;

    def isTransparent(self):
        return True

    def actUp(self):
        self.act(self.x, self.y, self.x, self.y - 1)

    def actDown(self):
        self.act(self.x, self.y, self.x, self.y + 1)

    def actLeft(self):
        self.act(self.x, self.y, self.x - 1, self.y)

    def actRight(self):
        self.act(self.x, self.y, self.x + 1, self.y)

    def act(self, fromX, fromY, x, y):
        if self.field.canMoveTo(x, y, self):
            self.field.moveTo(self, x, y)
            self.notifyMovement(fromX, fromY)
        elif self.field.canBeInteractedWith(x, y):
            self.field.interact(x, y)


    def addMoney(self, amount):
        self.money += amount

        self.notifyMoneyChange(self.money - amount)

    def setHasTarget(self, value):
        self.hasTarget = value

        if value:
            self.notifyGotTarget()

    def subscribe(self, observer):
        self.observers.append(observer)

    def notifyMovement(self, oldX, oldY):
        for observer in self.observers:
            observer.characterMoved(oldX, oldY, self.x, self.y)

    def notifyMoneyChange(self, oldMoney):
        for observer in self.observers:
            observer.characterMoneyChanged(oldMoney, self.money)

    def notifyGotTarget(self):
        for observer in self.observers:
            observer.characterGotTarget()
