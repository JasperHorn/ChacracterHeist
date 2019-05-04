
from .Door import Door

class VaultDoor(Door):
    def __init__(self, code):
        self.opened = False
        self.code = code
        self.codeCracked = [False] * len(code)

    def canBeInteractedWith(self, character):
        return not self.opened

    def interact(self, character):
        character.startCrackingVaultDoor(self)

    def isPassable(self, character):
        return self.opened

    def getCodeLength(self):
        return len(self.code)

    def getCodeDigit(self, n):
        return self.code[n]

    def isCodeDigitCracked(self, n):
        return self.codeCracked[n]
