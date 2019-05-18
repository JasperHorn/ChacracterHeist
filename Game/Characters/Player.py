
from .Character import Character

class Player(Character):

    def __init__(self, field, x, y):
        super().__init__(field, x, y)

        self.observers = []
        self.money = 0
        self.hasTarget = False
        self.exited = False
        self.crackingVaultDoor = None
        self.captured = False

    def crack(self, number):
        if not self.crackingVaultDoor is None:
            self.crackingVaultDoor.crack(self, number)

    def addMoney(self, amount):
        self.money += amount

        self.notifyMoneyChange(self.money - amount)

    def setHasTarget(self, value):
        self.hasTarget = value

        if value:
            self.notifyGotTarget()

    def capture(self):
        self.captured = True

    def startCrackingVaultDoor(self, vaultDoor):
        self.crackingVaultDoor = vaultDoor
        self.notifyStartCrackingVaultDoor()

    def stopCrackingVaultDoor(self):
        self.crackingVaultDoor = None
        self.notifyStopCrackingVaultDoor()

    def subscribe(self, observer):
        self.observers.append(observer)

    def notifyMovement(self, oldX, oldY):
        for observer in self.observers:
            observer.characterMoved(oldX, oldY, self.x, self.y)

    def notifyMoneyChange(self, oldMoney):
        for observer in self.observers:
            observer.characterMoneyChanged(oldMoney, self.money)

    def notifyGotTarget(self):
        for observer in self.observers:
            observer.characterGotTarget()

    def notifyStartCrackingVaultDoor(self):
        for observer in self.observers:
            observer.characterStartedCracking(self.crackingVaultDoor)

    def notifyStopCrackingVaultDoor(self):
        for observer in self.observers:
            observer.characterStoppedCracking()
