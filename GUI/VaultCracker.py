
import consoleUtils

from CharacterObserver import CharacterObserver
from colorama import Fore, Back, Style

class VaultCracker(CharacterObserver):
    width = 16
    height = 9

    def __init__(self, character, x, y):
        self.x = x
        self.y = y
        character.subscribe(self)

    def characterStartedCracking(self, vaultDoor):
        self.vaultDoor = vaultDoor

        consoleUtils.specialPrint(self.y, self.x, ' ' * self.width, Back.RED)
        for y in range(1, self.height - 1):
            consoleUtils.specialPrint(self.y + y, self.x, ' ', Back.RED)
            consoleUtils.specialPrint(self.y + y, self.x + self.width - 1, ' ', Back.RED)
        consoleUtils.specialPrint(self.y + self.height - 1, self.x, ' ' * self.width, Back.RED)

        consoleUtils.specialPrint(self.y + 2, self.x + 2, 'Cracking', Fore.YELLOW + Style.BRIGHT)
        consoleUtils.specialPrint(self.y + 4, self.x + 2, 'Press digits', Fore.GREEN)
        self.printCrackStatus()

    def printCrackStatus(self):
        for n in range(0, self.vaultDoor.getCodeLength()):
            if self.vaultDoor.isCodeDigitCracked(n):
                consoleUtils.specialPrint(self.y + 6, self.x + 2 + n, str(self.vaultDoor.getCodeDigit(n)), Fore.GREEN + Style.BRIGHT)
            else:
                consoleUtils.specialPrint(self.y + 6, self.x + 2 + n, '?', Fore.RED + Style.BRIGHT)

    def characterStoppedCracking(self):
        for dy in range(0, self.height):
            consoleUtils.specialPrint(self.y + dy, self.x, ' ' * self.width)
