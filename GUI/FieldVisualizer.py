
import colorama

import consoleUtils

from Game.Objects import Wall, Money, TargetTreasure
from CharacterObserver import CharacterObserver

class FieldVisualizer(CharacterObserver):

    offset = (3, 2)

    def __init__(self, field, character):
        consoleUtils.clearScreen()
        colorama.init()

        for x in range(0, field.width):
            for y in range(0, field.height):
                object = field.getObjectAtLocation(x, y)
                if isinstance(object, Wall):
                    consoleUtils.printAtPosition(FieldVisualizer.offset[1] + y, FieldVisualizer.offset[0] + x, 'X')
                elif isinstance(object, Money):
                    consoleUtils.printAtPosition(FieldVisualizer.offset[1] + y, FieldVisualizer.offset[0] + x, '$')
                elif isinstance(object, TargetTreasure):
                    consoleUtils.printAtPosition(FieldVisualizer.offset[1] + y, FieldVisualizer.offset[0] + x, '*')

        consoleUtils.printAtPosition(FieldVisualizer.offset[1] + character.y, FieldVisualizer.offset[0] + character.x, '@')

    def characterMoved(self, oldX, oldY, newX, newY):
        consoleUtils.printAtPosition(FieldVisualizer.offset[1] + oldY, FieldVisualizer.offset[0] + oldX, ' ')
        consoleUtils.printAtPosition(FieldVisualizer.offset[1] + newY, FieldVisualizer.offset[0] + newX, '@')
