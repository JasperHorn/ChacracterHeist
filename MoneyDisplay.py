
import consoleUtils

from CharacterObserver import CharacterObserver

class MoneyDisplay(CharacterObserver):
    def __init__(self, character, x, y):
        self.x = x
        self.y = y
        self.writeMoney(character.money)
        character.subscribe(self)

    def writeMoney(self, money):
        consoleUtils.setCursorPosition(self.y, self.x)
        consoleUtils.printPartial('$' + str(money))
        consoleUtils.setCursorPosition(25, 70)

    def characterMoneyChanged(self, oldMoney, newMoney):
        consoleUtils.setCursorPosition(self.y, self.x + 1)
        for n in range(0, len(str(oldMoney))):
            consoleUtils.printPartial(' ')

        self.writeMoney(newMoney)
