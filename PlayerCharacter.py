
class PlayerCharacter:

    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def moveUp(self):
        if self.y > 1:
            self.y -= 1

    def moveDown(self):
        if self.y < 20:
            self.y += 1

    def moveLeft(self):
        if self.x > 1:
            self.x -= 1

    def moveRight(self):
        if self.x < 20:
            self.x += 1
