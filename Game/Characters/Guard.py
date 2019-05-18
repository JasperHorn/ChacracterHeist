
import random

from .Character import Character

class Guard(Character):
    def stepOn(self, character):
        if character.isPlayer():
            character.capture()

    def getVisibilityPriority(self):
        return 100010

    def move(self):
        direction = random.randint(0, 3)

        if direction == 0:
            self.actUp()
        elif direction == 1:
            self.actDown()
        elif direction == 2:
            self.actLeft()
        elif direction == 3:
            self.actRight()
