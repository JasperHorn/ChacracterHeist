
class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.objects = {}
        self.squares = []
        for x in range(0, width):
            row = []
            for y in range(0, height):
                row.append(None);
            self.squares.append(row)

    def addObject(self, x, y, object):
        self.squares[x][y] = object
        self.objects[object] = (x, y)
        object.setField(self)

    def removeObject(self, object):
        x, y = self.objects[object]
        del self.objects[object]
        self.squares[x][y] = None

    def canMoveTo(self, x, y, character):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        elif self.squares[x][y] is None:
            return True
        else:
            return self.squares[x][y].isPassable(character)

    def moveTo(self, character, x, y):
        if not (self.squares[x][y] is None):
            self.squares[x][y].stepOn(character)

    def getObjectAtLocation(self, x, y):
        return self.squares[x][y]
