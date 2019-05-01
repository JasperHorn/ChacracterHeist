
import colorama

import consoleUtils

class FieldVisualizer:

    idleCursor = (25, 70)

    def __init__(self, character):
        consoleUtils.clearScreen()
        colorama.init()

        consoleUtils.setCursorPosition(character.y, character.x)
        consoleUtils.printPartial('@')

        FieldVisualizer.resetCursor()

    def resetCursor():
        consoleUtils.setCursorPosition(FieldVisualizer.idleCursor[0], FieldVisualizer.idleCursor[1])

    def characterMoved(self, oldX, oldY, newX, newY):
        consoleUtils.setCursorPosition(oldY, oldX)
        consoleUtils.printPartial(' ')
        consoleUtils.setCursorPosition(newY, newX)
        consoleUtils.printPartial('@')

        FieldVisualizer.resetCursor()
