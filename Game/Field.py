
import consoleUtils

class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.observers = []

        self.objects = {}
        self.squares = []
        for x in range(0, width):
            row = []
            for y in range(0, height):
                row.append([]);
            self.squares.append(row)

    def subscribe(self, observer):
        self.observers.append(observer)

    def addObject(self, x, y, object):
        self.squares[x][y].append(object)
        self.objects[object] = (x, y)
        object.setField(self)
        self.notifyPositionChanged(x, y)

    def removeObject(self, object):
        x, y = self.objects[object]
        del self.objects[object]
        self.squares[x][y].remove(object)
        self.notifyPositionChanged(x, y)

    def canMoveTo(self, x, y, character):
        if not self.inBounds(x, y):
            return False
        else:
            return all(obj.isPassable(character) for obj in self.squares[x][y])

    def moveTo(self, character, x, y):
        self.squares[character.x][character.y].remove(character)
        self.notifyPositionChanged(character.x, character.y)

        character.x = x
        character.y = y
        self.squares[x][y].append(character)
        self.notifyPositionChanged(x, y)

        for object in self.squares[x][y]:
            object.stepOn(character)

    def getVisibleObjectAtLocation(self, x, y):
        square = self.squares[x][y]
        return max(square, key = lambda obj: obj.getVisibilityPriority(),
                   default = None);

    def inBounds(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def spreadViewingFromPoint(self, x, y):
        for object in self.squares[x][y]:
            object.view()

        viewQueue = [(x, y)]
        viewPoints = {(x, y)}

        while viewQueue:
            point = viewQueue.pop(0)

            object = self.getVisibleObjectAtLocation(point[0], point[1])
            if (object is not None):
                object.view()
            while object != self.getVisibleObjectAtLocation(point[0], point[1]):
                object = self.getVisibleObjectAtLocation(point[0], point[1])
                if (object is not None):
                    object.view()

            if object is None or object.isTransparent():
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        newPoint = (point[0] + dx, point[1] + dy)
                        if not newPoint in viewPoints and self.inBounds(newPoint[0], newPoint[1]):
                            viewQueue.append(newPoint)
                            viewPoints.add(newPoint)

    def notifyPositionChanged(self, x, y):
        for observer in self.observers:
            observer.fieldPositionChanged(x, y)
