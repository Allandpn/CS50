from pyfiglet import Figlet
import sys
import random



def aleatorio():
    return random.randint(0, len(Figlet().getFonts()))



def printOut(fonte):
    texto = input('Input: ')
    print('Output: ')

    figlet = Figlet()
    figlet.setFont(font = fonte)

    print(figlet.renderText(texto))



def main():


    list = Figlet().getFonts()

    if len(sys.argv) == 1:
        font = list[aleatorio()]
        printOut(font)

    elif len(sys.argv) == 3:
        if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in list:
                printOut(sys.argv[2])
        else:
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')

