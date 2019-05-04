
from .Object import Object
from .OpenedVaultDoor import OpenedVaultDoor

class VaultDoor(Object):
    def __init__(self, code):
        self.code = code
        self.codeCracked = [False] * len(code)
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def canBeInteractedWith(self, character):
        return True

    def interact(self, character):
        character.startCrackingVaultDoor(self)

    def isPassable(self, character):
        return False

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

                self.notifyCrackedStatusChanged()

                if all(self.codeCracked):
                    self.open = True
                    character.stopCrackingVaultDoor()
                    self.field.replaceObject(self, OpenedVaultDoor());

                return

    def notifyCrackedStatusChanged(self):
        for observer in self.observers:
            observer.vaultDoorCrackedStatusChanged()
