
import readchar
import colorama

import consoleUtils

consoleUtils.clearScreen()
colorama.init()

characterX = 1;
characterY = 1;

consoleUtils.setCursorPosition(characterY, characterX)
consoleUtils.printPartial('@')

while True:
    input = readchar.readkey()
    previousX = characterX
    previousY = characterY

    if input == '\x1b[D': # left arrow
        if characterX > 1:
            characterX -= 1
    elif input == '\x1b[C': # right arrow
        if characterX < 20:
            characterX += 1
    elif input == '\x1b[A': # up arrow
        if characterY > 1:
            characterY -= 1
    elif input == '\x1b[B': # down arrow
        if characterY < 20:
            characterY += 1

    if characterX != previousX or characterY != previousY:
        consoleUtils.setCursorPosition(previousY, previousX)
        consoleUtils.printPartial(' ')
        consoleUtils.setCursorPosition(characterY, characterX)
        consoleUtils.printPartial('@')
        consoleUtils.setCursorPosition(25, 70)
