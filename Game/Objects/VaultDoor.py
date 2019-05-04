
from .Door import Door

class VaultDoor(Door):
    def __init__(self):
        self.opened = False

    def canBeInteractedWith(self):
        return not self.opened

    def interact(self):
        self.opened = True

    def isPassable(self, character):
        return self.opened
