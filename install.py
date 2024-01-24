import os
import pyfiglet
import random
import sys
import time
from termcolor import colored
from colorama import Fore, Style

os.system("clear")

print('''
    ____           __        ____
   /  _/___  _____/ /_____ _/ / /
   / // __ \/ ___/ __/ __ `/ / / 
 _/ // / / (__  ) /_/ /_/ / / /  
/___/_/ /_/____/\__/\__,_/_/_/   
''')

def wait_with_spinner(seconds):
    symbols = "/-|\\"

    for _ in range(int(seconds)):
        for symbol in symbols:
            sys.stdout.write(f"\r[+] Please wait... {symbol}  ")
            sys.stdout.flush()
            time.sleep(0.25)

    sys.stdout.write("\r" + " " * 20 + "\r")

wait_time = 1.0
wait_with_spinner(wait_time)

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

animation = [f"{Fore.WHITE}Please wait{Fore.RED} [□□□□□□□□□□]0%",f"{Fore.WHITE}pLease wait {Fore.RED}[■□□□□□□□□□]10%",f"{Fore.WHITE}plEase wait{Fore.RED} [■■□□□□□□□□]20%", f"{Fore.WHITE}pleAse wait{Fore.RED} [■■■□□□□□□□]30%", f"{Fore.WHITE}pleaSe wait{Fore.YELLOW} [■■■■□□□□□□]40%", f"{Fore.WHITE}pleasE wait{Fore.YELLOW} [■■■■■□□□□□]50%", f"{Fore.WHITE}please Wait{Fore.BLUE} [■■■■■■□□□□]60%", f"{Fore.WHITE}please wAit{Fore.BLUE} [■■■■■■■□□□]70%", f"{Fore.WHITE}please waIt{Fore.CYAN} [■■■■■■■■□□]80%", f"{Fore.WHITE}please waiT{Fore.GREEN} [■■■■■■■■■□]90%", f"{Fore.GREEN}[+] Complete [■■■■■■■■■■]100%{Style.RESET_ALL}"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")
