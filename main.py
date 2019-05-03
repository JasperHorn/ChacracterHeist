
import readchar

import sampleField

from Game import PlayerCharacter
from GUI import FieldVisualizer
from GUI.HUD import MoneyDisplay, TargetDisplay

field = sampleField.create()
character = PlayerCharacter(field, 2, 2)

visualizer = FieldVisualizer(field, character)
moneyDisplay = MoneyDisplay(character, 35, 3)
moneyDisplay = TargetDisplay(character, 35, 5)

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
    print('You stole the target and won the game!')
else:
    print('You exited the game without winning.')
