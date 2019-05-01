
class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.squares = []
        for x in range(0, width):
            row = []
            for y in range(0, height):
                row.append(None);
            self.squares.append(row)

    def addObject(self, x, y, object):
        self.squares[x][y] = object

    def canMoveTo(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        else:
            return self.squares[x][y] is None

    def getObjectAtLocation(self, x, y):
        return self.squares[x][y]
