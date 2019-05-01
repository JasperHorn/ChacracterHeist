
import os


def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def setCursorPosition(x, y):
    printPartial('\x1b[%d;%dH' % (x, y))

def printPartial(text):
    print(text, end = '', flush = True)

def printAtPosition(x, y, text):
    setCursorPosition(x, y)
    printPartial(text)
