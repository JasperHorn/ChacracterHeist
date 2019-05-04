
from .Door import Door

class VaultDoor(Door):
    def __init__(self):
        self.opened = False

    def canBeInteractedWith(self, character):
        return not self.opened

    def interact(self, character):
        character.startCrackingVaultDoor(self)

    def isPassable(self, character):
        return self.opened
