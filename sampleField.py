
from Game import Field
from Game.Objects import Money, Wall

width = 30
height = 20

def create():
    field = Field(width, height)

    for x in range(0, width):
        field.addObject(x, 0, Wall())
        field.addObject(x, height - 1, Wall())

    for y in range(1, height - 1):
        field.addObject(0, y, Wall())
        field.addObject(width - 1, y, Wall())

    # Starting room
    for x in range(1, 8):
        field.addObject(x, 8, Wall())
    for y in range(1, 8):
        if y != 5:
            field.addObject(7, y, Wall())

    # Middle wall
    for y in range(1, height - 1):
        if y != 15:
            field.addObject(15, y, Wall())

    # Top right room
    for x in range(16, width - 1):
        if x != width - 3:
            field.addObject(x, 6, Wall())

    for y in range(2, 5):
        field.addObject(19, y, Money(10))

    return field
