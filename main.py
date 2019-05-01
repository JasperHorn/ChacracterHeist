
import readchar

import sampleField

from PlayerCharacter import PlayerCharacter
from FieldVisualizer import FieldVisualizer

field = sampleField.create()
character = PlayerCharacter(field, 2, 2)

visualizer = FieldVisualizer(field, character)

character.subscribe(visualizer)

while True:
    input = readchar.readkey()

    if input == '\x1b[D': # left arrow
        character.moveLeft()
    elif input == '\x1b[C': # right arrow
        character.moveRight()
    elif input == '\x1b[A': # up arrow
        character.moveUp()
    elif input == '\x1b[B': # down arrow
        character.moveDown()
