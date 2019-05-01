
import os

def printPartial(text):
    print(text, end = '', flush = True)

def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def setCursorPosition(x, y):
    printPartial('\x1b[%d;%dH' % (x, y))
