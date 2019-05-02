
import colorama

import consoleUtils

from Game.Objects import Wall, Money, TargetTreasure, Exit
from CharacterObserver import CharacterObserver
from colorama import Style, Fore, Back

class FieldVisualizer(CharacterObserver):

    offset = (3, 2)

    def __init__(self, field, character):
        consoleUtils.clearScreen()
        colorama.init()

        for x in range(0, field.width):
            for y in range(0, field.height):
                object = field.getObjectAtLocation(x, y)
                if isinstance(object, Wall):
                    consoleUtils.specialPrint(FieldVisualizer.offset[1] + y, FieldVisualizer.offset[0] + x, 'X', Fore.WHITE + Back.BLUE)
                elif isinstance(object, Money):
                    consoleUtils.specialPrint(FieldVisualizer.offset[1] + y, FieldVisualizer.offset[0] + x, '$', Fore.YELLOW + Style.BRIGHT)
                elif isinstance(object, TargetTreasure):
                    consoleUtils.specialPrint(FieldVisualizer.offset[1] + y, FieldVisualizer.offset[0] + x, '*', Fore.GREEN + Style.BRIGHT)
                elif isinstance(object, Exit):
                    consoleUtils.specialPrint(FieldVisualizer.offset[1] + y, FieldVisualizer.offset[0] + x, '↓', Fore.CYAN)

        consoleUtils.specialPrint(FieldVisualizer.offset[1] + character.y, FieldVisualizer.offset[0] + character.x, '@', Fore.CYAN)

    def characterMoved(self, oldX, oldY, newX, newY):
        consoleUtils.specialPrint(FieldVisualizer.offset[1] + oldY, FieldVisualizer.offset[0] + oldX, ' ')
        consoleUtils.specialPrint(FieldVisualizer.offset[1] + newY, FieldVisualizer.offset[0] + newX, '@', Fore.CYAN)
