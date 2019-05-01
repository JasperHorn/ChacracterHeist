
class PlayerCharacter:

    def __init__(self, field, x, y):
        self.field = field
        self.x = x
        self.y = y
        self.observers = []
        self.money = 0
        self.hasTarget = False
        self.exited = False

    def moveUp(self):
        if self.field.canMoveTo(self.x, self.y - 1, self):
            self.y -= 1
            self.field.moveTo(self, self.x, self.y)
            self.notifyMovement(self.x, self.y + 1)

    def moveDown(self):
        if self.field.canMoveTo(self.x, self.y + 1, self):
            self.y += 1
            self.field.moveTo(self, self.x, self.y)
            self.notifyMovement(self.x, self.y - 1)

    def moveLeft(self):
        if self.field.canMoveTo(self.x - 1, self.y, self):
            self.x -= 1
            self.field.moveTo(self, self.x, self.y)
            self.notifyMovement(self.x + 1, self.y)

    def moveRight(self):
        if self.field.canMoveTo(self.x + 1, self.y, self):
            self.x += 1
            self.field.moveTo(self, self.x, self.y)
            self.notifyMovement(self.x - 1, self.y)

    def addMoney(self, amount):
        self.money += amount

        self.notifyMoneyChange(self.money - amount)

    def setHasTarget(self, value):
        self.hasTarget = value

    def subscribe(self, observer):
        self.observers.append(observer)

    def notifyMovement(self, oldX, oldY):
        for observer in self.observers:
            observer.characterMoved(oldX, oldY, self.x, self.y)

    def notifyMoneyChange(self, oldMoney):
        for observer in self.observers:
            observer.characterMoneyChanged(oldMoney, self.money)
