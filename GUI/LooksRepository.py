
from colorama import Back

class LooksRepository:
    def __init__(self):
        self.symbols = {}
        self.styles = {}

    def defineObjectLook(self, objectType, symbol, style):
        self.symbols[objectType] = symbol
        self.styles[objectType] = style

    def getObjectSymbol(self, object):
        if type(object) in self.symbols:
            return self.symbols[type(object)]
        else:
            return ' '

    def getObjectStyle(self, object):
        if type(object) in self.styles:
            return self.styles[type(object)]
        else:
            return Back.BLACK
