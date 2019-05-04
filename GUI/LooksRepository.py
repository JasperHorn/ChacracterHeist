
from Game.Objects import Wall, Money, TargetTreasure, Exit, Door

class LooksRepository:
    def __init__(self):
        self.symbols = {}

        self.symbols[Wall] = 'X'
        self.symbols[Money] = '$'
        self.symbols[TargetTreasure] = '*'
        self.symbols[Exit] = 'O'
        self.symbols[Door] = 'Z'

    def getObjectSymbol(self, object):
        if type(object) in self.symbols:
            return self.symbols[type(object)]
        else:
            return ' '
