
from .MoneyDisplay import MoneyDisplay
from .TargetDisplay import TargetDisplay

class HUD:
    def __init__(self, character, x, y):
        self.moneyDisplay = MoneyDisplay(character, x + 1, y + 1);
        self.targetDisplay = TargetDisplay(character, x + 1, y + 3);
