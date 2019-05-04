
from colorama import Style, Fore, Back
from Game.Objects import Wall, Money, TargetTreasure, Exit, Door

class LooksRepository:
    def __init__(self):
        self.symbols = {}
        self.styles = {}

        self.symbols[Wall] = 'X'
        self.symbols[Money] = '$'
        self.symbols[TargetTreasure] = '*'
        self.symbols[Exit] = 'O'
        self.symbols[Door] = 'Z'

        self.styles[Wall] = Fore.WHITE + Back.BLUE
        self.styles[Money] = Fore.YELLOW + Style.BRIGHT + Back.BLACK
        self.styles[TargetTreasure] = Fore.GREEN + Style.BRIGHT + Back.BLACK
        self.styles[Exit] = Fore.CYAN + Back.BLUE
        self.styles[Door] = Fore.GREEN + Back.BLUE

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
