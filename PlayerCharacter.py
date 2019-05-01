
class PlayerCharacter:

    def __init__(self, field, x, y):
        self.field = field
        self.x = x
        self.y = y
        self.observers = []

    def moveUp(self):
        if self.field.canMoveTo(self.x, self.y - 1):
            self.y -= 1
            self.notifyMovement(self.x, self.y + 1)

    def moveDown(self):
        if self.field.canMoveTo(self.x, self.y + 1):
            self.y += 1
            self.notifyMovement(self.x, self.y - 1)

    def moveLeft(self):
        if self.field.canMoveTo(self.x - 1, self.y):
            self.x -= 1
            self.notifyMovement(self.x + 1, self.y)

    def moveRight(self):
        if self.field.canMoveTo(self.x + 1, self.y):
            self.x += 1
            self.notifyMovement(self.x - 1, self.y)

    def subscribe(self, observer):
        self.observers.append(observer)

    def notifyMovement(self, oldX, oldY):
        for observer in self.observers:
            observer.characterMoved(oldX, oldY, self.x, self.y)
