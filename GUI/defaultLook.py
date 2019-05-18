
from colorama import Style, Fore, Back
from Game.Objects import Wall, Money, TargetTreasure, Exit, Door, FogOfWar
from Game.Objects import VaultDoor, OpenedVaultDoor, Guard
from Game import PlayerCharacter

from .LooksRepository import LooksRepository
from .TargetAcquiredLookMutator import TargetAcquiredLookMutator

defaultLook = LooksRepository()

defaultLook.defineObjectLook(Wall, 'X', Fore.WHITE + Back.BLUE)
defaultLook.defineObjectLook(Money, '$', Fore.YELLOW + Style.BRIGHT + Back.BLACK)
defaultLook.defineObjectLook(TargetTreasure, '*', Fore.GREEN + Style.BRIGHT + Back.BLACK)
defaultLook.defineObjectLook(Exit, 'O', Fore.CYAN + Back.BLUE)
defaultLook.defineObjectLook(Door, 'Z', Fore.GREEN + Back.BLUE)
defaultLook.defineObjectLook(FogOfWar, '.', Fore.BLACK + Style.BRIGHT + Back.BLACK)
defaultLook.defineObjectLook(PlayerCharacter, '@', Fore.CYAN + Back.BLACK)
defaultLook.defineObjectLook(VaultDoor, 'N', Fore.CYAN + Style.BRIGHT + Back.BLUE)
defaultLook.defineObjectLook(OpenedVaultDoor, 'N', Fore.GREEN + Back.BLUE)
defaultLook.defineObjectLook(Guard, 'G', Fore.RED + Style.BRIGHT + Back.BLACK)

lookMutators = []

def initDefaultLookMutators(visualizer, character):
    mutator = TargetAcquiredLookMutator(defaultLook, visualizer, character,
                                        Exit, 'O', Fore.GREEN + Style.BRIGHT + Back.BLACK)
    lookMutators.append(mutator)
