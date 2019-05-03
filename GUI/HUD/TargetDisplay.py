
import consoleUtils

from CharacterObserver import CharacterObserver
from colorama import Style, Fore

class TargetDisplay(CharacterObserver):
    def __init__(self, character, x, y):
        self.x = x
        self.y = y
        character.subscribe(self)

    def characterGotTarget(self):
        consoleUtils.specialPrint(self.y, self.x, '*', Fore.GREEN + Style.BRIGHT)
