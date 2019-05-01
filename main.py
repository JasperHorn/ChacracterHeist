
import readchar
import colorama
import os

def printPartial(text):
    print(text, end = '', flush = True)

def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def setCursorPosition(x, y):
    printPartial('\x1b[%d;%dH' % (x, y))

clearScreen()
colorama.init()

characterX = 1;
characterY = 1;

setCursorPosition(characterY, characterX)
printPartial('@')

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
        setCursorPosition(previousY, previousX)
        printPartial(' ')
        setCursorPosition(characterY, characterX)
        printPartial('@')
        setCursorPosition(25, 70)
