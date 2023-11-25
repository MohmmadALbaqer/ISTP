import os
import pyfiglet
import random
from termcolor import colored

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

selected_color = random.choice(colors)

text = 'I N S T A L L'

lo = pyfiglet.figlet_format(text)
colored_lo = colored(lo, color=selected_color)

print(colored_lo)

os.system("pip install speedtest-cli")
os.system("pip install pyfiglet")
os.system("pip install psutil")
os.system("pip install termcolor")
os.system("pip install colorama")
os.system("pip install tqdm")
os.system("pip install init")
os.system("pip install Style")
os.system("pip install Fore")
