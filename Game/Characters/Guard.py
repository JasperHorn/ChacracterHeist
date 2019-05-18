
import random

from .Character import Character

class Guard(Character):
    def __init__(self, field, x, y):
        super().__init__(field, x, y)

        self.followingWall = None

    def stepOn(self, character):
        if character.isPlayer():
            character.capture()

    def getVisibilityPriority(self):
        return 100010

    def move(self):
        if self.followingWall is None:
            self.findWallToFollow()

        # The previous function tries to modify this, so it might have changed
        if self.followingWall is None:
            self.defaultMove()
        else:
            self.moveAlongWall()

        player = self.field.getPlayerIfAtLocation(self.x, self.y)
        if player is not None:
            self.stepOn(player)

    def defaultMove(self):
        self.actUp()

    def findWallToFollow(self):
        pass

    def moveAlongWall(self):
        pass
