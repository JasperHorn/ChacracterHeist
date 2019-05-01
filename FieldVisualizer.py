
import colorama

import consoleUtils

from Wall import Wall

class FieldVisualizer:

    idleCursor = (25, 70)
    offset = (3, 2)

    def __init__(self, field, character):
        consoleUtils.clearScreen()
        colorama.init()

        for x in range(0, field.width):
            for y in range(0, field.height):
                if isinstance(field.getObjectAtLocation(x, y), Wall):
                    consoleUtils.setCursorPosition(FieldVisualizer.offset[1] + y, FieldVisualizer.offset[0] + x)
                    consoleUtils.printPartial('X')

        consoleUtils.setCursorPosition(FieldVisualizer.offset[1] + character.y, FieldVisualizer.offset[0] + character.x)
        consoleUtils.printPartial('@')

        FieldVisualizer.resetCursor()

    def resetCursor():
        consoleUtils.setCursorPosition(FieldVisualizer.idleCursor[0], FieldVisualizer.idleCursor[1])

    def characterMoved(self, oldX, oldY, newX, newY):
        consoleUtils.setCursorPosition(FieldVisualizer.offset[1] + oldY, FieldVisualizer.offset[0] + oldX)
        consoleUtils.printPartial(' ')
        consoleUtils.setCursorPosition(FieldVisualizer.offset[1] + newY, FieldVisualizer.offset[0] + newX)
        consoleUtils.printPartial('@')

        FieldVisualizer.resetCursor()
