
from .Object import Object

class Door(Object):
    def stepOn(self, character):
        if character.isPlayer():
            for dx in [-1, 1]:
                for dy in [-1, 1]:
                    self.field.spreadViewingFromPoint(character.x + dx, character.y + dy)

    def shouldPatrolAlong(self, guard):
        return True
