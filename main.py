
import readchar
import colorama

import sampleField
import consoleUtils

from Game import PlayerCharacter
from GUI import FieldVisualizer, VaultCracker, drawIntroScreen
from GUI import defaultLook, initDefaultLookMutators
from GUI.HUD import HUD

colorama.init()
consoleUtils.clearScreen()

drawIntroScreen()
readchar.readkey();

field = sampleField.create()
character = PlayerCharacter(field, 2, 2)
field.spreadViewingFromPoint(character.x, character.y)

consoleUtils.clearScreen()

visualizer = FieldVisualizer(defaultLook, field, character)
initDefaultLookMutators(visualizer, character)
hud = HUD(character, 34, 2)
vaultCracker = VaultCracker(character, 47, 2)

while not character.exited:
    input = readchar.readkey()

    if input == '\x1b[D': # left arrow
        character.actLeft()
    elif input == '\x1b[C': # right arrow
        character.actRight()
    elif input == '\x1b[A': # up arrow
        character.actUp()
    elif input == '\x1b[B': # down arrow
        character.actDown()
    elif input == '0':
        character.crack(0)
    elif input == '1':
        character.crack(1)
    elif input == '2':
        character.crack(2)
    elif input == '3':
        character.crack(3)
    elif input == '4':
        character.crack(4)
    elif input == '5':
        character.crack(5)
    elif input == '6':
        character.crack(6)
    elif input == '7':
        character.crack(7)
    elif input == '8':
        character.crack(8)
    elif input == '9':
        character.crack(9)
    elif input == 'q':
        break;
    elif input == 'a':
        field.getVisibleObjectAtLocation(character.x, character.y, True)

print()

if character.exited:
    print('You stole the treasure and won the game!')
else:
    print('You exited the game without winning.')
