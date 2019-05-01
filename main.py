
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

printPartial("Your character: ")

while True:
    input = readchar.readkey()
    setCursorPosition(1, 17)

    if len(input) == 1:
        printPartial(input)
    else:
        # Print as a list, so it doesn't get interpreted as ANSI code...
        printPartial(list(input))
