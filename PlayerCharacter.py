
class PlayerCharacter:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.observers = []

    def moveUp(self):
        if self.y > 1:
            self.y -= 1
            self.notifyMovement(self.x, self.y + 1)

    def moveDown(self):
        if self.y < 20:
            self.y += 1
            self.notifyMovement(self.x, self.y - 1)

    def moveLeft(self):
        if self.x > 1:
            self.x -= 1
            self.notifyMovement(self.x + 1, self.y)

    def moveRight(self):
        if self.x < 20:
            self.x += 1
            self.notifyMovement(self.x - 1, self.y)

    def subscribe(self, observer):
        self.observers.append(observer)

    def notifyMovement(self, oldX, oldY):
        for observer in self.observers:
            observer.characterMoved(oldX, oldY, self.x, self.y)
