import sys
import os
import time
import speedtest
import requests
from time import sleep
from tqdm import tqdm
from colorama import Fore, Style, Back, init
from termcolor import colored
from prettytable import PrettyTable

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white
Y = '\033[33m'  # yellow
B = '\033[34m'  # blue
M = '\033[35m'  # magenta
D = '\033[30m'  # dark or black

def clear_screen():
    operating_system = os.name

    try:
        if operating_system == 'posix': 
            os.system('clear')
        elif operating_system == 'nt': 
            os.system('cls')
        else:
            print("Unsupported operating system.")
    except Exception as e:
        print(f"An error occurred: {e}")

clear_screen()

def spin():
    delay = 0.25
    spinner = ['█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█']

    for _ in range(1):
        for i in spinner:
            message = f"[*] {Fore.BLUE}Checking your internet connection...[{i}]{Style.RESET_ALL}"
            colored_message = colored(message, 'blue', attrs=['bold'])
            sys.stdout.write(f"\r{colored_message}   ")
            sys.stdout.flush()
            time.sleep(delay)

    sys.stdout.write("\r")
    sys.stdout.flush()
    done_message = colored("[+] Your Internet connection has been verified", 'yellow', attrs=['bold'])
    sys.stdout.write("\033[K") 
    print(done_message)
    time.sleep(1)

spin()

def check_internet_connection():
    try:
        response = requests.get('http://www.google.com', timeout=5)
        return True
    except requests.ConnectionError:
        return False

if check_internet_connection():
    print(f"{Fore.GREEN}[*] Internet connection is available. You can proceed with execution.{Style.RESET_ALL}")
    time.sleep(0.25)
    os.system("clear")
else:
    print(f"{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}]{Fore.RED} No internet connection !{Style.RESET_ALL}")
    exit()

print(rf"""
      {G}\ | /      
     {B}-- {R}O{B} --{W}
       {G}/|\        {B}____________________________{W}                                      
      {G}/\|/\      {B}/   _____/__    ___/______   \{W}
     {G}/  |  \     {B}\_____  \  |    |   |     ___/{W} 
    {G}/\/\|/\/\    {B}/        \ |    |   |    |{W}  
   {G}/    |    \  {B}/_______  / |____|   |____|{Y} Version : 4{W}
  {B}-     -     -{W}         {B}\/{W}""")
print(f'''
{Fore.RED}+------------------------------------------------------------------+
{Fore.RED}|{Fore.GREEN} GitHub{Fore.WHITE} : {Fore.BLUE}MohmmadALbaqer {Fore.WHITE}|{Fore.YELLOW} https://www.github.com/MohmmadALbaqer/ {Fore.RED}|
{Fore.RED}|{Fore.GREEN} Instagram{Fore.WHITE} :{Fore.BLUE} r94xs {Fore.WHITE}      |{Fore.YELLOW} https://www.instagram.com/r94xs/       {Fore.RED}|
{Fore.RED}+------------------------------------------------------------------+{Style.RESET_ALL}''')

init(autoreset=True)
print(f"{Fore.WHITE}[{Fore.GREEN}*{Fore.WHITE}] {Fore.BLUE}Downloading to servers and information at internet speed{Style.RESET_ALL}")
print(1*"\n")
st = speedtest.Speedtest()
st.get_best_server()

for _ in tqdm(range(10), colour="green", desc="Finding Optimal Server"):
    sleep(0.05)

st.download()
for _ in tqdm(range(10), colour="yellow", desc="Getting Download Speed"):
    sleep(0.05)

st.upload()
for _ in tqdm(range(10), colour="red", desc="Getting Upload Speed"):
    sleep(0.05)

res_dict = st.results.dict()

dwnl = f"{res_dict['download'] / 10**6:.2f}"
upl = f"{res_dict['upload'] / 10**6:.2f}"

table = PrettyTable()

table.field_names = [f"{Fore.MAGENTA}ID{Style.RESET_ALL}", f"{Fore.BLUE}INFORMATION{Style.RESET_ALL}", f"{Fore.RED}Information results{Style.RESET_ALL}"]

table.add_row([f"{Fore.GREEN}1{Style.RESET_ALL}", f"{Fore.YELLOW}Download{Style.RESET_ALL}", f"{dwnl} Mbps ({float(dwnl) * 0.125:.2f} MB/s)"])
table.add_row([f"{Fore.GREEN}2{Style.RESET_ALL}", f"{Fore.YELLOW}Upload{Style.RESET_ALL}", f"{upl} Mbps ({float(upl) * 0.125:.2f} MB/s)"])
table.add_row([f"{Fore.GREEN}3{Style.RESET_ALL}", f"{Fore.YELLOW}Ping{Style.RESET_ALL}", f"{res_dict['ping']:.2f} ms"])
table.add_row([f"{Fore.GREEN}4{Style.RESET_ALL}", f"{Fore.YELLOW}HOST{Style.RESET_ALL}", res_dict['server']['host']])
table.add_row([f"{Fore.GREEN}5{Style.RESET_ALL}", f"{Fore.YELLOW}SPONSOR{Style.RESET_ALL}", res_dict['server']['sponsor']])
table.add_row([f"{Fore.GREEN}6{Style.RESET_ALL}", f"{Fore.YELLOW}LATENCY{Style.RESET_ALL}", f"{res_dict['server']['latency']:.2f} ms"])

for field in table.field_names:
    table.align[field] = "l"

print(table)
