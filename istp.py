import sys
import os
import time
import datetime
import speedtest
import requests
from time import sleep
from tqdm import tqdm
from colorama import Fore, Style, Back, init
from termcolor import colored
from prettytable import PrettyTable

init()

R = f"{Fore.RED}{Style.BRIGHT}"
G = f"{Fore.GREEN}{Style.BRIGHT}"
B = f"{Fore.BLUE}{Style.BRIGHT}"
Y = f"{Fore.YELLOW}{Style.BRIGHT}"
C = f"{Fore.CYAN}{Style.BRIGHT}"
M = f"{Fore.MAGENTA}{Style.BRIGHT}"
W = f"{Fore.WHITE}{Style.BRIGHT}"
D = f"{Fore.BLACK}{Style.BRIGHT}"
ERROR = f"{Y}[{R}!{Y}]{R}"
INFO = f"{Fore.BLUE}{Style.BRIGHT}[{Fore.GREEN}{Style.BRIGHT}INFO{Fore.BLUE}{Style.BRIGHT}]{Fore.MAGENTA}"

def clear_screen():
    operating_system = os.name
    try:
        if operating_system == 'posix': 
            os.system('clear')
        elif operating_system == 'nt': 
            os.system('cls')
        else:
            print(f"[!] System unknown!{Style.RESET_ALL}")
    except Exception as e:
        print(f"[ERROR]{W}: {e}")
clear_screen()

def spin():
    delay = 0.25
    spinner = ['█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█']

    for _ in range(1):
        for i in spinner:
            message = f"[*] {B}Checking your internet connection...[{i}]{W}"
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
    print(f"{G}[*] Internet connection is available. You can proceed with execution.{W}")
    time.sleep(0.25)
else:
    print(f"{ERROR} No internet connection !{W}")
    exit()

def clear_screen():
    operating_system = os.name
    try:
        if operating_system == 'posix': 
            os.system('clear')
        elif operating_system == 'nt': 
            os.system('cls')
        else:
            print(f"[!] System unknown!{Style.RESET_ALL}")
    except Exception as e:
        print(f"[ERROR]{W}: {e}")
clear_screen()

print(rf"""
      {G}\ | /      
     {B}-- {R}O{B} --{W}
       {G}/|\        {B}___  ____________________________{W}                                      
      {G}/\|/\      {B}|   |/   _____/__    ___/______   \{W}
     {G}/  |  \     {B}|   |\_____  \  |    |   |     ___/{W} 
    {G}/\/\|/\/\    {B}|   |/        \ |    |   |    |{W}  
   {G}/    |    \  {B} |___|_______  / |____|   |____|{Y} Version : 5{W}
  {B}-     -     -{W}              {B}\/{W}
{Back.RED}{W} [Internet Speed Test Ping ] {Style.RESET_ALL}
{R}+------------------------------------------------------------------+
{R}|{G} GitHub{W} : {B}MohmmadALbaqer {W}|{Y} https://www.github.com/MohmmadALbaqer/ {R}|
{R}|{G} Instagram{W} :{B} r94xs {W}      |{Y} https://www.instagram.com/r94xs/       {R}|
{R}+------------------------------------------------------------------+{W}""")

init(autoreset=True)
print(f"{Fore.BLUE}[{G}*{B}] {Y}Downloading to servers and information at internet speed.{W}")
st = speedtest.Speedtest()
st.get_best_server()

for _ in tqdm(range(10), colour="green", desc=f"{INFO} Finding  Optimal  Server"):
    sleep(0.05)

st.download()
for _ in tqdm(range(10), colour="yellow", desc=f"{INFO} Getting {W}[{Y}Download{W}] {M}Speed"):
    sleep(0.05)

st.upload()
for _ in tqdm(range(10), colour="red", desc=f"{INFO} Getting  {W}[{Y}Upload{W}] {M} Speed"):
    sleep(0.05)

res_dict = st.results.dict()

dwnl = f"{res_dict['download'] / 10**6:.2f}"
upl = f"{res_dict['upload'] / 10**6:.2f}"

table = PrettyTable()

table.field_names = [f"{M}ID{W}", f"{B}INFORMATION{W}", f"{R}Information results{W}"]

table.add_row([f"{G}1{W}", f"{Y}Download{W}", f"{B}{dwnl} {M}Mbps{W} ({B}{float(dwnl) * 0.125:.2f} {G}MB/s{W})"])
table.add_row([f"{G}2{W}", f"{Y}Upload{W}", f"{B}{upl} {M}Mbps{W} ({B}{float(upl) * 0.125:.2f} {G}MB/s{W})"])
table.add_row([f"{G}3{W}", f"{Y}Ping{W}", f"{B}{res_dict['ping']:.2f} {G}ms{W}"])
table.add_row([f"{G}4{W}", f"{Y}HOST{W}", res_dict['server']['host']])
table.add_row([f"{G}5{W}", f"{Y}SPONSOR{W}", res_dict['server']['sponsor']])
table.add_row([f"{G}6{W}", f"{Y}LATENCY{W}", f"{B}{res_dict['server']['latency']:.2f} {G}ms{W}"])
table.add_row([f"{G}7{W}", f"{Y}ISP{W}", res_dict['client']['isp']])
table.add_row([f"{G}8{W}", f"{Y}Country{W}", res_dict['client']['country']])
table.add_row([f"{G}9{W}", f"{Y}URL{W}", st.results.share()])
table.add_row([f"{G}10{W}", f"{Y}Hosted By{W}", res_dict['server']['host']])
packet_loss = res_dict.get('packetLoss', 'N/A')
table.add_row([f"{G}11{W}", f"{Y}Packet Loss{W}", f"{B}{packet_loss}%{W}"])
table.add_row([f"{G}12{W}", f"{Y}Server ID{W}", res_dict['server']['id']])
table.add_row([f"{G}13{W}", f"{Y}ISP Rating{W}", res_dict['client']['isprating']])

for field in table.field_names:
    table.align[field] = "l"

print(table)

now = datetime.datetime.now()
formatted_time = now.strftime("%I:%M %p")
formatted_day = now.strftime("%A")
print(f"{B}[{G}Today{B}] {W}({Y}{formatted_day}{W} {M}{now:%B %D %Y}{W}) {B}[{G}Time{B}] {Y}[{R}{formatted_time}{Y}]{W}")
