
from .Door import Door

class VaultDoor(Door):
    def __init__(self, code):
        self.open = False
        self.code = code
        self.codeCracked = [False] * len(code)

    def canBeInteractedWith(self, character):
        return not self.open

    def interact(self, character):
        character.startCrackingVaultDoor(self)

    def isPassable(self, character):
        return self.open

    def getCodeLength(self):
        return len(self.code)

    def getCodeDigit(self, n):
        return self.code[n]

    def isCodeDigitCracked(self, n):
        return self.codeCracked[n]

    def crack(self, character, number):
        for n in range(0, len(self.code)):
            if (not self.codeCracked[n]) and self.code[n] == number:
                self.codeCracked[n] = True

                if all(self.codeCracked):
                    self.open = True
                    character.stopCrackingVaultDoor()
                
                return
