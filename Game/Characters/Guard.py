
import random

import consoleUtils

from .Character import Character
from Vector import Vector
from coordinateUtils import crossByDistance, filledManhattanCircle

class Guard(Character):
    def __init__(self, field, x, y):
        super().__init__(field, x, y)

        self.patrolDirection = None
        self.target = None
        
    def stepOn(self, character):
        if character.isPlayer():
            character.capture()

    def getVisibilityPriority(self):
        return 100010

    def move(self):
        self.seekOutTarget()
        
        if self.target is None and self.patrolDirection is None:
            self.findWallToFollow()

        if self.target is not None:
            self.moveTowardsTarget()
        # findWallToFollow() tries to modify this, so it might have changed
        elif self.patrolDirection is not None:
            self.patrolMove()
        else:
            self.defaultMove()

        player = self.field.getPlayerIfAtLocation(self.x, self.y)
        if player is not None:
            self.stepOn(player)

    def defaultMove(self):
        self.actUp()

    def findWallToFollow(self):
        for lookAt in crossByDistance(2):
            if self.followable(Vector(self.x, self.y) + lookAt):
                newDirection = lookAt.unitize().rotateCounterClockwise()
                self.patrolDirection = newDirection
                return
    
    def seekOutTarget(self):
        for (x, y) in filledManhattanCircle(3):
            player = self.field.getPlayerIfAtLocation(self.x + x, self.y + y)
            
            if player is not None:
                self.target = Vector(self.x + x, self.y + y)

    def moveTowardsTarget(self):
        if self.target.x > self.x and self.canMoveRight():
            self.actRight()
        elif self.target.x < self.x and self.canMoveLeft():
            self.actLeft()
        elif self.target.y > self.y and self.canMoveDown():
            self.actDown()
        elif self.target.y < self.y and self.canMoveUp():
            self.actUp()
        else:
            self.target = None
        
        self.patrolDirection = None;
        if self.target is not None:
            if self.x == self.target.x and self.y == self.target.y:
                self.target = None
    
    def canMoveDown(self):
        return self.canMoveTo(self.x, self.y + 1)

    def canMoveUp(self):
        return self.canMoveTo(self.x, self.y - 1)

    def canMoveRight(self):
        return self.canMoveTo(self.x + 1, self.y)

    def canMoveLeft(self):
        return self.canMoveTo(self.x - 1, self.y)
    
    def canMoveTo(self, x, y):
        return self.field.canMoveTo(x, y, self)

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
        return self.field.shouldPatrolAlong(vector.x, vector.y, self)
