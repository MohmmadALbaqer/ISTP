import os 
import sys
import time 
from time import sleep
from colorama import Fore, Style
from termcolor import colored
import pyfiglet
import random

os.system("clear")

colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

selected_color = random.choice(colors)

text = 'UPDATE'

lo = pyfiglet.figlet_format(text)
colored_lo = colored(lo, color=selected_color)

print(colored_lo)

def wait_with_spinner(seconds):
    symbols = "/-|\\"

    for _ in range(int(seconds)):
        for symbol in symbols:
            sys.stdout.write(f"\r[+] Please wait... {symbol}  ")
            sys.stdout.flush()
            time.sleep(0.25)

    sys.stdout.write("\r" + " " * 20 + "\r")

wait_time = 2.5
wait_with_spinner(wait_time)


os.system("git pull origin master")
