
import readchar
import colorama

import consoleUtils
from PlayerCharacter import PlayerCharacter

consoleUtils.clearScreen()
colorama.init()

character = PlayerCharacter(1, 1)

consoleUtils.setCursorPosition(character.y, character.x)
consoleUtils.printPartial('@')

while True:
    input = readchar.readkey()
    previousX = character.x
    previousY = character.y

    if input == '\x1b[D': # left arrow
        character.moveLeft()
    elif input == '\x1b[C': # right arrow
        character.moveRight()
    elif input == '\x1b[A': # up arrow
        character.moveUp()
    elif input == '\x1b[B': # down arrow
        character.moveDown()

    if character.x != previousX or character.y != previousY:
        consoleUtils.setCursorPosition(previousY, previousX)
        consoleUtils.printPartial(' ')
        consoleUtils.setCursorPosition(character.y, character.x)
        consoleUtils.printPartial('@')
        consoleUtils.setCursorPosition(25, 70)
