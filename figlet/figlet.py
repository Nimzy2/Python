import sys
import random
import pyfiglet
if len(sys.argv) != 1 or len(sys.argv)!=3:
    sys.exit("invalid usage.Enter zero or two command line arguments")
if len(sys.argv) == 3:
    if sys.argv[1] != "--font" or sys.argv[1] != "--f": 
        sys.exit("Invalid usage. The first command_line -f or --font")

text = input("Enter any text: ")

# instantciate an objet of type Figlet
figlet = pyfiglet.Figlet()  

if len(sys.argv) == 1:
    fonts = figlet.getFonts()
    random_font = random.choice(fonts)
    figlet.setFont(font = random_font)
    print(figlet.renderText(text))
elif len(sys.argv) == 3:  
    fonts = figlet.getFonts()
    user_font = sys.argv[2]
    figlet.setFont(font = user_font)
    print(figlet.renderText(text))

    
# print(fonts)
# print(len(fonts))
# for font in fonts:
#     print(font)
