
import random

import consoleUtils

from .Character import Character

class Guard(Character):
    def __init__(self, field, x, y):
        super().__init__(field, x, y)

        self.patrolDirection = None

    def stepOn(self, character):
        if character.isPlayer():
            character.capture()

    def getVisibilityPriority(self):
        return 100010

    def move(self):
        if self.patrolDirection is None:
            self.findWallToFollow()

        # The previous function tries to modify this, so it might have changed
        if self.patrolDirection is None:
            self.defaultMove()
        else:
            self.patrolMove()

        player = self.field.getPlayerIfAtLocation(self.x, self.y)
        if player is not None:
            self.stepOn(player)

    def defaultMove(self):
        self.actUp()

    def findWallToFollow(self):
        for (x, y) in self.searchArea(2):
            if self.followable(self.x + x, self.y + y):
                self.patrolDirection = self.unitize(self.rotateCounterClockwise((x, y)))
                return

    def unitize(self, vector):
        x = vector[0]
        y = vector[1]

        if x != 0:
            x = int(x / abs(x))

        if y != 0:
            y = int(y / abs(y))

        return (x, y)

    def searchArea(self, radius):
        for distance in range(1, radius + 1):
            for coordinate in self.manhattanCirle(distance):
                yield coordinate

    def manhattanCirle(self, radius):
        for n in range(0, radius * 4):
            # Start (0, -r) instead of (r, 0)
            n = (n - radius) % (radius * 4)

            if n <= radius * 2:
                x = radius - n
                y = radius - abs(x)
            else:
                x = -3 * radius + n
                y = -radius + abs(x)
            yield (x, y)

    def patrolMove(self):
        twoAhead = (self.x + self.patrolDirection[0] * 2, self.y + self.patrolDirection[1] * 2)
        if self.followable(twoAhead[0], twoAhead[1]):
            self.patrolDirection = self.rotateCounterClockwise(self.patrolDirection)

        clockwise = self.rotateClockwise(self.patrolDirection)
        aroundCorner = (self.x + clockwise[0] * 2, self.y + clockwise[1] * 2)
        wallGapAroundCorner = (aroundCorner[0] + self.patrolDirection[0] * -1, aroundCorner[1] + self.patrolDirection[1] * -1)
        corner = (wallGapAroundCorner[0] + self.patrolDirection[0] * -1, wallGapAroundCorner[1] + self.patrolDirection[1] * -1)

        if (not self.followable(aroundCorner[0], aroundCorner[1]) and not self.followable(wallGapAroundCorner[0], wallGapAroundCorner[1]) and self.followable(corner[0], corner[1])):
            self.patrolDirection = self.rotateClockwise(self.patrolDirection)

        self.act(self.x, self.y, self.x + self.patrolDirection[0], self.y + self.patrolDirection[1])

    def followable(self, x, y):
        return self.field.getVisibleObjectAtLocation(x, y) is not None

    def rotateCounterClockwise(self, direction):
        return (direction[1], direction[0] * -1)

    def rotateClockwise(self, direction):
        return (direction[1] * -1, direction[0])
