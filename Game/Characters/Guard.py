
import random

import consoleUtils

from .Character import Character
from Vector import Vector
from coordinateUtils import filledManhattanCircle

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
        for (x, y) in filledManhattanCircle(2):
            if self.followable(Vector(self.x + x, self.y + y)):
                newDirection = Vector(x, y).unitize().rotateCounterClockwise()
                self.patrolDirection = newDirection
                return

    def patrolMove(self):
        changedDirection = False

        if not changedDirection:
            changedDirection = self.rotateWithConvexCorner()
        if not changedDirection:
            changedDirection = self.rotateAroundConcaveCorner()

        self.act(self.x,
                 self.y,
                 self.x + self.patrolDirection.x,
                 self.y + self.patrolDirection.y)

    def rotateWithConvexCorner(self):
        twoAhead = Vector(self.x, self.y) + self.patrolDirection * 2
        if self.followable(twoAhead):
            self.patrolDirection = self.patrolDirection.rotateCounterClockwise()
            return True

        return False

    def rotateAroundConcaveCorner(self):
        clockwise = self.patrolDirection.rotateClockwise()
        aroundCorner = Vector(self.x, self.y) + clockwise * 2
        wallGapAroundCorner = aroundCorner + self.patrolDirection * -1
        corner = wallGapAroundCorner + self.patrolDirection * -1

        if (not self.followable(aroundCorner)
                and not self.followable(wallGapAroundCorner)
                and self.followable(corner)):
            self.patrolDirection = self.patrolDirection.rotateClockwise()
            return True

        return False

    def followable(self, vector):
        object = self.field.getVisibleObjectAtLocation(vector.x, vector.y)
        return object is not None
