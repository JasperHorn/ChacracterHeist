
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, n):
        return Vector(self.x * n, self.y * n)

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def rotateClockwise(self):
        return Vector(self.y * -1, self.x)

    def rotateCounterClockwise(self):
        return Vector(self.y, self.x * -1)

    def unitize(self):
        if self.x == 0:
            x = 0
        else:
            x = int(self.x / abs(self.x))

        if self.y == 0:
            y = 0
        else:
            y = int(self.y / abs(self.y))

        return Vector(x, y)
