
from Wall import Wall
from Field import Field

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

    return field
