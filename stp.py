import sys
import os
import time
import speedtest
import subprocess
import getpass
import random
import pyfiglet
from time import sleep
from tqdm import tqdm
from colorama import Fore, Style, init
from termcolor import colored

os.system("clear")

def wait_with_spinner(seconds):
    symbols = "/-|\\"

    for _ in range(int(seconds)):
        for symbol in symbols:
            sys.stdout.write(f"\rPlease wait {symbol}  ")
            sys.stdout.flush()
            time.sleep(0.25)

    sys.stdout.write("\r" + " " * 20 + "\r")

wait_time = 2.5
wait_with_spinner(wait_time)

colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

selected_color = random.choice(colors)

text = 'S T P'

lo = pyfiglet.figlet_format(text)
colored_lo = colored(lo, color=selected_color)

print(colored_lo)

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



insta_text = (
    "+----------------------------------------------------+\n"
    f"{Fore.RED}INSTAGRAM{Fore.YELLOW} ==> {Fore.CYAN}https://www.instagram.com/r94xs/{Style.RESET_ALL}   \n"
    f"{Fore.RED}GitHub{Fore.YELLOW} =====> {Fore.CYAN}https://www.github.com/MohmmadALbaqer/{Style.RESET_ALL}   \n"
    "+----------------------------------------------------+"
)
print(insta_text)


def print_loading():
    loading_text = colored("[*]", "blue") + colored("Loading", "red") + colored("...", "yellow")
    
    for char in loading_text:
        print(char, end='', flush=True)
        time.sleep(0.1)

print_loading()

print("")

required_libraries = ["speedtest-cli", "pyfiglet", "psutil"]

missing_libraries = []

for library in required_libraries:
    try:
        result = subprocess.check_output(["pip", "show", library], text=True)
    except subprocess.CalledProcessError:
        missing_libraries.append(library)

if not missing_libraries:

    password = getpass.getpass("Enter the access code: ")

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
else:
    for library in missing_libraries:
        try:
            subprocess.check_call(["pip", "install", library])
            print(f"{library} installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred during installation of {library}: {e}")

text = "For more, write a command \"python3 help.py -h\" "

start_index = text.find("python3 help.py -h")
if start_index != -1:
    end_index = start_index + len("python3 help.py -h")
    colored_text = text[:start_index] + colored(text[start_index:end_index], "yellow") + text[end_index:]
    print(colored_text)
else:
    print(text)
