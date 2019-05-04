
import colorama

import consoleUtils

from CharacterObserver import CharacterObserver
from colorama import Style, Fore, Back

class FieldVisualizer(CharacterObserver):

    offset = (3, 2)

    def __init__(self, look, field, character):
        self.field = field
        self.look = look

        for x in range(0, field.width):
            for y in range(0, field.height):
                self.drawObjectAtLocation(x, y)

        consoleUtils.specialPrint(FieldVisualizer.offset[1] + character.y, FieldVisualizer.offset[0] + character.x, '@', Fore.CYAN + Back.BLACK)

    def characterMoved(self, oldX, oldY, newX, newY):
        self.drawObjectAtLocation(oldX, oldY)
        consoleUtils.specialPrint(FieldVisualizer.offset[1] + newY, FieldVisualizer.offset[0] + newX, '@', Fore.CYAN + Back.BLACK)

    def redraw(self, objectType):
        for x in range(0, self.field.width):
            for y in range(0, self.field.height):
                if isinstance(self.field.getObjectAtLocation(x, y), objectType):
                    self.drawObjectAtLocation(x, y)

    def drawObjectAtLocation(self, x, y):
        object = self.field.getObjectAtLocation(x, y)
        symbol = self.look.getObjectSymbol(object)
        style = self.look.getObjectStyle(object)

        consoleUtils.specialPrint(FieldVisualizer.offset[1] + y, FieldVisualizer.offset[0] + x, symbol, style)
