
import readchar
import colorama

import sampleField
import consoleUtils

from Game import EnemyManager
from Game.Characters import Player
from GUI import FieldVisualizer, VaultCracker, drawIntroScreen
from GUI import defaultLook, initDefaultLookMutators
from GUI.HUD import HUD

colorama.init()
consoleUtils.clearScreen()

drawIntroScreen()
readchar.readkey()

enemyManager = EnemyManager()

field = sampleField.create(enemyManager)
character = Player(field, 2, 2)
field.spreadViewingFromPoint(character.x, character.y)

consoleUtils.clearScreen()

visualizer = FieldVisualizer(defaultLook, field, character)
initDefaultLookMutators(visualizer, character)
hud = HUD(character, 34, 2)
vaultCracker = VaultCracker(character, 47, 2)

while not character.exited and not character.captured:
    input = readchar.readkey()

    acted = False

    if input == '\x1b[D': # left arrow
        acted = character.actLeft()
    elif input == '\x1b[C': # right arrow
        acted = character.actRight()
    elif input == '\x1b[A': # up arrow
        acted = character.actUp()
    elif input == '\x1b[B': # down arrow
        acted = character.actDown()
    elif input == '0':
        acted = character.crack(0)
    elif input == '1':
        acted = character.crack(1)
    elif input == '2':
        acted = character.crack(2)
    elif input == '3':
        acted = character.crack(3)
    elif input == '4':
        acted = character.crack(4)
    elif input == '5':
        acted = character.crack(5)
    elif input == '6':
        acted = character.crack(6)
    elif input == '7':
        acted = character.crack(7)
    elif input == '8':
        acted = character.crack(8)
    elif input == '9':
        acted = character.crack(9)
    elif input == 'q':
        break;

    if acted and not character.captured:
        enemyManager.move()

print()

if character.exited:
    print('You stole the treasure and won the game!')
elif character.captured:
    print('You were captured. Game over.')
else:
    print('You exited the game without winning.')
