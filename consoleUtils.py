
import os

from colorama import Style

idleCursor = (25, 70)

def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def setCursorPosition(x, y):
    printPartial('\x1b[%d;%dH' % (x, y))

def printPartial(text):
    print(text, end = '', flush = True)

def resetCursor():
    setCursorPosition(idleCursor[0], idleCursor[1])

def specialPrint(x, y, text, styling = None):
    setCursorPosition(x, y)
    if not styling is None:
        printPartial(styling)
    printPartial(text)
    if not styling is None:
        printPartial(Style.RESET_ALL)
    resetCursor()
