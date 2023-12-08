import os
import pyfiglet
import random
import sys
import time
from termcolor import colored
os.system("clear")

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

selected_color = random.choice(colors)

text = 'Install'

lo = pyfiglet.figlet_format(text)
colored_lo = colored(lo, color=selected_color)

print(colored_lo)

def wait_with_spinner(seconds):
    symbols = "/-|\\"

    for _ in range(int(seconds)):
        for symbol in symbols:
            sys.stdout.write(f"\rPlease wait {symbol}  ")
            sys.stdout.flush()
            time.sleep(0.25)

    sys.stdout.write("\r" + " " * 20 + "\r")

wait_time = 1.0
wait_with_spinner(wait_time)


def print_loading():
    loading_text = colored("[*]", "blue") + colored("Loading", "red") + colored("...", "yellow")
    
    for char in loading_text:
        print(char, end='', flush=True)
        time.sleep(0.1)

print_loading()

print(1*"\n")

os.system("pip install speedtest-cli")
os.system("pip install pyfiglet")
os.system("pip install psutil")
os.system("pip install termcolor")
os.system("pip install colorama")
os.system("pip install tqdm")
os.system("pip install init")
os.system("pip install Style")
os.system("pip install Fore")
os.system("chmod +x stp.py")
os.system("chmod +x update.py")
os.system("chmod +x help.py")
os.system("chmod +x install.py")

def print_loading():
    loading_text = colored("[*]", "red") + colored("Done", "green") + colored("Installation", "yellow")
    
    for char in loading_text:
        print(char, end='', flush=True)
        time.sleep(0.1)

print_loading()
