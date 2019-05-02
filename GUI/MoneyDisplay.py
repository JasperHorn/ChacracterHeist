
import consoleUtils

from CharacterObserver import CharacterObserver
from colorama import Style, Fore

class MoneyDisplay(CharacterObserver):
    def __init__(self, character, x, y):
        self.x = x
        self.y = y
        self.writeMoney(character.money)
        character.subscribe(self)

    def writeMoney(self, money):
        consoleUtils.specialPrint(self.y, self.x, '$' + str(money), Fore.YELLOW + Style.BRIGHT)

    def characterMoneyChanged(self, oldMoney, newMoney):
        consoleUtils.specialPrint(self.y, self.x + 1, ' ' * len(str(oldMoney)))

        self.writeMoney(newMoney)
