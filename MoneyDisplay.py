
import consoleUtils

from CharacterObserver import CharacterObserver

class MoneyDisplay(CharacterObserver):
    def __init__(self, character, x, y):
        self.x = x
        self.y = y
        self.writeMoney(character.money)
        character.subscribe(self)

    def writeMoney(self, money):
        consoleUtils.printAtPosition(self.y, self.x, '$' + str(money))

    def characterMoneyChanged(self, oldMoney, newMoney):
        consoleUtils.printAtPosition(self.y, self.x + 1, ' ' * len(str(oldMoney)))

        self.writeMoney(newMoney)
