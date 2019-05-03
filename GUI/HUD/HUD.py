
import consoleUtils

from colorama import Back

from .MoneyDisplay import MoneyDisplay
from .TargetDisplay import TargetDisplay

class HUD:
    background = Back.BLUE
    height = 7
    width = 10

    def __init__(self, character, x, y):
        self.x = x
        self.y = y

        self.drawBackground()

        self.moneyDisplay = MoneyDisplay(character, x + 2, y + 2, HUD.background);
        self.targetDisplay = TargetDisplay(character, x + 2, y + 4, HUD.background);

    def drawBackground(self):
        for dy in range(0, HUD.height):
            consoleUtils.specialPrint(self.y + dy, self.x, ' ' * HUD.width, HUD.background)
