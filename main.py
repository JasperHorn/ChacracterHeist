
import readchar
import colorama

import sampleField
import consoleUtils

from Game import PlayerCharacter
from GUI import FieldVisualizer, drawIntroScreen
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

character.subscribe(visualizer)

while not character.exited:
    input = readchar.readkey()

    if input == '\x1b[D': # left arrow
        character.moveLeft()
    elif input == '\x1b[C': # right arrow
        character.moveRight()
    elif input == '\x1b[A': # up arrow
        character.moveUp()
    elif input == '\x1b[B': # down arrow
        character.moveDown()
    elif input == 'q':
        break;

print()

if character.exited:
    print('You stole the treasure and won the game!')
else:
    print('You exited the game without winning.')
