
import os

idleCursor = (25, 70)

def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def setCursorPosition(x, y):
    printPartial('\x1b[%d;%dH' % (x, y))

def printPartial(text):
    print(text, end = '', flush = True)

def resetCursor():
    setCursorPosition(idleCursor[0], idleCursor[1])

def printAtPosition(x, y, text):
    setCursorPosition(x, y)
    printPartial(text)
    resetCursor()
