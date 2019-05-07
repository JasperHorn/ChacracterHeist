
import consoleUtils

from colorama import Back, Fore, Style

def drawIntroScreen():
    consoleUtils.specialPrint(4, 15, 'Welcome to ' + Fore.RED + Style.BRIGHT + 'CharacterHeist' + Style.RESET_ALL)
    consoleUtils.specialPrint(8, 4, 'In this game:')
    consoleUtils.specialPrint(10, 4, '- This is you: ' + Fore.CYAN + '@' + Style.RESET_ALL)
    consoleUtils.specialPrint(12, 4, '- You have to acquire the treasure: ' + Fore.GREEN + Style.BRIGHT + '*' + Style.RESET_ALL)
    consoleUtils.specialPrint(14, 4, '- Next you have to escape: ' + Fore.GREEN + Style.BRIGHT + 'O' + Style.RESET_ALL)
    consoleUtils.specialPrint(16, 4, '- You will have to crack and move through vault and normal doors: ' + Fore.CYAN + Style.BRIGHT + 'N' + Style.RESET_ALL + ' & ' + Fore.GREEN + 'Z' + Style.RESET_ALL)
    consoleUtils.specialPrint(18, 4, '- You should collect money on your way: ' + Fore.YELLOW + Style.BRIGHT + '$' + Style.RESET_ALL)
    consoleUtils.specialPrint(22, 20, "Press any button to continue")
