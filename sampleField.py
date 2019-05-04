
from Game import Field
from Game.Objects import Money, Wall, TargetTreasure, Exit, Door, FogOfWar
from Game.Objects import VaultDoor

width = 30
height = 20

def create():
    field = Field(width, height)

    for x in range(0, width):
        field.addObject(x, 0, Wall())
        if x == 3:
            field.addObject(x, height - 1, Exit())
        else:
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
        if y == 15:
            field.addObject(15, y, Door())
        else:
            field.addObject(15, y, Wall())

    # Top right room
    for x in range(16, width - 1):
        if x == width - 3:
            field.addObject(x, 6, Door())
        else:
            field.addObject(x, 6, Wall())

    # Vault
    for y in range(1, 6):
        if y == 3:
            field.addObject(21, y, VaultDoor([1, 2, 3, 4]))
        else:
            field.addObject(21, y, Wall())

    for y in range(2, 5):
        field.addObject(19, y, Money(10))

    field.addObject(17, 3, TargetTreasure())

    # Fog of war
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            field.addObject(x, y, FogOfWar())

    return field
