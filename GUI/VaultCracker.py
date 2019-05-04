
import consoleUtils

from CharacterObserver import CharacterObserver
from colorama import Fore, Back, Style

class VaultCracker(CharacterObserver):
    def __init__(self, character, x, y):
        self.x = x
        self.y = y
        character.subscribe(self)

    def characterStartedCracking(self, vaultDoor):
        consoleUtils.specialPrint(self.y, self.x, "Cracking Vault Door!", Fore.YELLOW + Style.BRIGHT)
