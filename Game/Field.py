
import consoleUtils

class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.objects = {}
        self.squares = []
        for x in range(0, width):
            row = []
            for y in range(0, height):
                row.append([]);
            self.squares.append(row)

    def addObject(self, x, y, object):
        self.squares[x][y].append(object)
        self.objects[object] = (x, y)
        object.setField(self)

    def removeObject(self, object):
        x, y = self.objects[object]
        del self.objects[object]
        self.squares[x][y].remove(object)

    def canMoveTo(self, x, y, character):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        else:
            return all(obj.isPassable(character) for obj in self.squares[x][y])

    def moveTo(self, character, x, y):
        for object in self.squares[x][y]:
            object.stepOn(character)

    def getVisibleObjectAtLocation(self, x, y):
        square = self.squares[x][y]
        return max(square, key = lambda obj: obj.getVisibilityPriority(),
                   default = None);
