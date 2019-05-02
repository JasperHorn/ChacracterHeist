
import consoleUtils

from CharacterObserver import CharacterObserver

class TargetDisplay(CharacterObserver):
    def __init__(self, character, x, y):
        self.x = x
        self.y = y
        character.subscribe(self)

    def characterGotTarget(self):
        consoleUtils.printAtPosition(self.y, self.x, '*')
