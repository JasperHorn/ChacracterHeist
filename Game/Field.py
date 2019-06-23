
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
        visible = self.getVisibleObjectAtLocation(x, y) is object
        self.notifyPositionChanged(x, y, visible)

    def removeObject(self, object):
        x, y = self.objects[object]
        visible = self.getVisibleObjectAtLocation(x, y) is object
        del self.objects[object]
        self.squares[x][y].remove(object)
        self.notifyPositionChanged(x, y, visible)

    def replaceObject(self, oldObject, newObject):
        x, y = self.objects[oldObject]
        del self.objects[oldObject]
        self.squares[x][y].remove(oldObject)
        self.addObject(x, y, newObject)

    def canMoveTo(self, x, y, character):
        if not self.inBounds(x, y):
            return False
        else:
            return all(obj.isPassable(character) for obj in self.squares[x][y])

    def moveTo(self, character, x, y):
        visible = self.getVisibleObjectAtLocation(character.x, character.y) is character
        self.squares[character.x][character.y].remove(character)
        self.notifyPositionChanged(character.x, character.y, visible)

        character.x = x
        character.y = y
        self.squares[x][y].append(character)
        visible = self.getVisibleObjectAtLocation(x, y) is character
        self.notifyPositionChanged(x, y, visible)

        for object in self.squares[x][y]:
            object.stepOn(character)

    def canBeInteractedWith(self, x, y, character):
        if not self.inBounds(x, y):
            return False
        else:
            return any(obj.canBeInteractedWith(character) for obj in self.squares[x][y])

    def interact(self, x, y, character):
        for object in self.squares[x][y]:
            object.interact(character)

    def shouldPatrolAlong(self, x, y, guard):
        if not self.inBounds(x, y):
            return True
        else:
            return any(obj.shouldPatrolAlong(guard) for obj in self.squares[x][y])

    def getVisibleObjectAtLocation(self, x, y, print = False):
        square = self.squares[x][y]
        if print:
            consoleUtils.specialPrint(25, 1, square)
        return max(square, key = lambda obj: obj.getVisibilityPriority(),
                   default = None);

    def getPlayerIfAtLocation(self, x, y):
        if not self.inBounds(x, y):
            return None

        for object in self.squares[x][y]:
            if object.isPlayer():
                return object

        return None

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

    def notifyPositionChanged(self, x, y, visible):
        for observer in self.observers:
            observer.fieldPositionChanged(x, y, visible)
