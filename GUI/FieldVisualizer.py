
import colorama

import consoleUtils

from FieldObserver import FieldObserver

class FieldVisualizer(FieldObserver):

    offset = (3, 2)

    def __init__(self, look, field, character):
        self.field = field
        self.look = look

        field.subscribe(self)

        for x in range(0, field.width):
            for y in range(0, field.height):
                self.drawObjectAtLocation(x, y)

    def fieldPositionChanged(self, x, y):
        self.drawObjectAtLocation(x, y)

    def redraw(self, objectType):
        for x in range(0, self.field.width):
            for y in range(0, self.field.height):
                if isinstance(self.field.getVisibleObjectAtLocation(x, y), objectType):
                    self.drawObjectAtLocation(x, y)

    def drawObjectAtLocation(self, x, y):
        object = self.field.getVisibleObjectAtLocation(x, y)
        symbol = self.look.getObjectSymbol(object)
        style = self.look.getObjectStyle(object)

        consoleUtils.specialPrint(FieldVisualizer.offset[1] + y, FieldVisualizer.offset[0] + x, symbol, style)
