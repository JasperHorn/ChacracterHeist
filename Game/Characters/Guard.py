
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
        for (x, y) in self.searchArea(2):
            x += self.x
            y += self.y

            if self.field.getVisibleObjectAtLocation(x, y) is not None:
                self.followingWall = (x, y)

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

    def moveAlongWall(self):
        pass
