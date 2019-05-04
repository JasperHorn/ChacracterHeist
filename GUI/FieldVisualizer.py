
import colorama

import consoleUtils

from Game.Objects import Wall, Money, TargetTreasure, Exit, Door
from CharacterObserver import CharacterObserver
from colorama import Style, Fore, Back
from .LooksRepository import LooksRepository

class FieldVisualizer(CharacterObserver):

    offset = (3, 2)

    def __init__(self, field, character):
        self.field = field
        self.looks = LooksRepository()

        for x in range(0, field.width):
            for y in range(0, field.height):
                self.drawObjectAtLocation(x, y)

        consoleUtils.specialPrint(FieldVisualizer.offset[1] + character.y, FieldVisualizer.offset[0] + character.x, '@', Fore.CYAN + Back.BLACK)

    def characterMoved(self, oldX, oldY, newX, newY):
        self.drawObjectAtLocation(oldX, oldY)
        consoleUtils.specialPrint(FieldVisualizer.offset[1] + newY, FieldVisualizer.offset[0] + newX, '@', Fore.CYAN + Back.BLACK)

    def characterGotTarget(self):
        for x in range(0, self.field.width):
            for y in range(0, self.field.height):
                if isinstance(self.field.getObjectAtLocation(x, y), Exit):
                    consoleUtils.specialPrint(FieldVisualizer.offset[1] + y, FieldVisualizer.offset[0] + x, 'O', Fore.GREEN + Style.BRIGHT + Back.BLACK)

    def drawObjectAtLocation(self, x, y):
        object = self.field.getObjectAtLocation(x, y)
        symbol = self.looks.getObjectSymbol(object)

        if object is None:
            style = Back.BLACK
        elif isinstance(object, Wall):
            style = Fore.WHITE + Back.BLUE
        elif isinstance(object, Money):
            style = Fore.YELLOW + Style.BRIGHT + Back.BLACK
        elif isinstance(object, TargetTreasure):
            style = Fore.GREEN + Style.BRIGHT + Back.BLACK
        elif isinstance(object, Exit):
            style = Fore.CYAN + Back.BLUE
        elif isinstance(object, Door):
            style = Fore.GREEN + Back.BLUE
        else:
            style = None

        consoleUtils.specialPrint(FieldVisualizer.offset[1] + y, FieldVisualizer.offset[0] + x, symbol, style)
