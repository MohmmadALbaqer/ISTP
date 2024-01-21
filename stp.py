import sys
import os
import time
import speedtest
import requests
import getpass
import random
from time import sleep
from tqdm import tqdm
from colorama import Fore, Style, init
from termcolor import colored
os.system("clear")

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
    time.sleep(3)

spin()

print(1*"\n")

def check_internet_connection():
    try:
        response = requests.get('http://www.google.com', timeout=5)
        return True
    except requests.ConnectionError:
        return False

if check_internet_connection():
    print(f"{Fore.GREEN}Internet connection is available. You can proceed with execution.{Style.RESET_ALL}")
    time.sleep(2)
    os.system("clear")
else:
    print(f"{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}]{Fore.RED} No internet connection !{Style.RESET_ALL}")
    exit()

text = '''
  ____________________________ 
 /   _____/__    ___/______   \\
 \_____  \  |    |   |     ___/
 /        \ |    |   |    |    
/_______  / |____|   |____|  Version : 2.1  
        \/                     
'''

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

random_color = random.choice(colors)

colored_text = colored(text, random_color)
print(colored_text)

art = '''
+----------------------------+
|  .               .         |
| .´  ·  .     .  ·  `.      |
| :  :  :  (¯)  :  :  :      |
| `.  ·  ` /¯\ ´  ·  .´      |
|   `     /¯¯¯\     ´        |
+----------------------------+
|     Speed Test Ping        |
+----------------------------+
'''

colored_art = colored(art, 'white')

colored_art = colored_art.replace('Speed', colored('Speed', 'green'))
colored_art = colored_art.replace('Test', colored('Test', 'red'))
colored_art = colored_art.replace('Ping', colored('Ping', 'yellow'))

print(colored_art)

print(f'''
 {Fore.RED}<--------------------------------------------------------------------->
 {Fore.RED}|{Fore.GREEN} GitHub{Fore.WHITE} : {Fore.BLUE}MohmmadALbaqer {Fore.WHITE}|{Fore.YELLOW}   https://www.github.com/MohmmadALbaqer/  {Fore.RED}|
 {Fore.RED}|{Fore.GREEN} Instagram{Fore.WHITE} :{Fore.BLUE} r94xs {Fore.WHITE}      |{Fore.YELLOW}   https://www.instagram.comr94xs/         {Fore.RED}|
 {Fore.RED}+---------------------------------------------------------------------+
{Style.RESET_ALL}''')

password = getpass.getpass(f"{Fore.GREEN}[+] Enter the access code: {Style.RESET_ALL}")

if password == "r94xs":
    init(autoreset=True)
    print(Fore.GREEN + "GETTING BEST AVAILABLE SERVERS, UPLOADING & DOWNLOADING SPEED.....")

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

    print("")
    print(Fore.MAGENTA + "="*80)
    print(Fore.GREEN + "INTERNET SPEED TEST RESULTS:".center(80))
    print(Fore.MAGENTA + "="*80)
    print(Fore.YELLOW + f"Download: {dwnl} Mbps ({float(dwnl) * 0.125:.2f} MB/s) | Upload: {upl} Mbps ({float(dwnl) * 0.125:.2f} MB/s) | Ping: {res_dict['ping']:.2f} ms".center(80))
    print(Fore.MAGENTA + "-"*80)
    print(Fore.CYAN + f"HOST: {res_dict['server']['host']} | SPONSOR: {res_dict['server']['sponsor']} | LATENCY: {res_dict['server']['latency']:.2f} ms".center(80))
    print(Fore.MAGENTA + "-"*80)
else:
    print("Access denied. The access code is incorrect.")

text = "For more, write a command \"python3 help.py -h\" "
start_index = text.find("python3 help.py -h")

if start_index != -1:
    end_index = start_index + len("python3 help.py -h")
    colored_text = text[:start_index] + colored(text[start_index:end_index], "yellow") + text[end_index:]
    print(colored_text)
else:
    print(text)
