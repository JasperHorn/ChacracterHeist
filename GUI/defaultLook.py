
from colorama import Style, Fore, Back
from Game.Objects import Wall, Money, TargetTreasure, Exit, Door

from .LooksRepository import LooksRepository

defaultLook = LooksRepository()

defaultLook.defineObjectLook(Wall, 'X', Fore.WHITE + Back.BLUE)
defaultLook.defineObjectLook(Money, '$', Fore.YELLOW + Style.BRIGHT + Back.BLACK)
defaultLook.defineObjectLook(TargetTreasure, '*', Fore.GREEN + Style.BRIGHT + Back.BLACK)
defaultLook.defineObjectLook(Exit, 'O', Fore.CYAN + Back.BLUE)
defaultLook.defineObjectLook(Door, 'Z', Fore.GREEN + Back.BLUE)
