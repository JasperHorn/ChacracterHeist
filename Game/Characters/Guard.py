
import random

import consoleUtils

from .Character import Character
from CharacterObserver import CharacterObserver
from Vector import Vector
from coordinateUtils import crossByDistance, filledManhattanCircle

horizontalThenVertical = [Vector(1, 0),
                          Vector(-1, 0),
                          Vector(0, 1),
                          Vector(0, -1)]

verticalThenHorizontal = [Vector(0, 1),
                          Vector(0, -1),
                          Vector(1, 0),
                          Vector(-1, 0)]

class Guard(Character):
    def __init__(self, field, x, y):
        super().__init__(field, x, y)

        self.patrolDirection = None
        self.target = None
        self.lastMoveTowardsTargetWasHorizontal = False
        self.lastPlayerMove = None
        
    def stepOn(self, character):
        if character.isPlayer():
            character.capture()

    def getVisibilityPriority(self):
        return 100010

    def isPassable(self, character):
        return character.isPlayer()

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
                self.lastPlayerMove = player.lastMove
                break;
            else:
                self.lastPlayerMove = None

    def moveTowardsTarget(self):
        if self.lastPlayerMove is not None:
            consoleUtils.specialPrint(23, 5, "Moving on same axis as player")
            # If player moved and was seen move on same axis
            if self.lastPlayerMove.x != 0:
                order = horizontalThenVertical
            else:
                order = verticalThenHorizontal
        else:
            consoleUtils.specialPrint(23, 5, "Alternating axes              ")
            # If player wasn't seen moving, move on different 
            # axis then last move
            if self.lastMoveTowardsTargetWasHorizontal:
                order = verticalThenHorizontal
            else:
                order = horizontalThenVertical
        
        moved = False
        
        for direction in order:
            coordinate = Vector(self.x, self.y) + direction
            
            if self.isCloserToTarget(coordinate) and self.canMoveTo(coordinate):
                self.act(self.x, self.y, coordinate.x, coordinate.y)
                moved = True
                
                if direction.x != 0:
                    self.lastMoveTowardsTargetWasHorizontal = True
                else:
                    self.lastMoveTowardsTargetWasHorizontal = False
                
                # Move only once    
                break
            
        if not moved:
            self.target = None
        
        self.patrolDirection = None
        if self.target is not None:
            if self.x == self.target.x and self.y == self.target.y:
                self.target = None

    def isCloserToTarget(self, coordinate):
        ownDistance = abs(self.target - Vector(self.x, self.y))
        coordinateDistance = abs(self.target - coordinate)
        
        return (coordinateDistance.x <= ownDistance.x 
                and coordinateDistance.y <= ownDistance.y) 

    def canMoveTo(self, to):
        return self.field.canMoveTo(to.x, to.y, self)

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
