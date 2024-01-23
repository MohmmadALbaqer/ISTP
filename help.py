import sys
import os
import time
import speedtest
import subprocess
import pyfiglet
import socket
from time import sleep
from tqdm import tqdm
from colorama import Fore, Style, init
import argparse
os.system("clear")

def show_banner():
   import pyfiglet
import random
from termcolor import colored

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

selected_color = random.choice(colors)

text = 'help'

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

def check_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1e+6
    upload_speed = st.upload() / 1e+6

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

def check_ping():
    host = "www.google.com"
    response = subprocess.call(["ping", host])

    if response == 0:
        print(f"Successfully connected to {host}")
    else:
        print(f"Failed to connect to {host}")

def display_provider():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    try:
        host = socket.gethostbyaddr(ip_address)
        print(f"Connected ISP Name: {host[0]}")
    except socket.herror:
        print("Failed to find the connected ISP name")

def main():
    parser = argparse.ArgumentParser(description='Internet Tool - A tool to check internet status')

    parser.add_argument('-s', '--speed', action='store_true', help='Check internet speed')
    parser.add_argument('-p', '--ping', action='store_true', help='Measure computer ping time')
    parser.add_argument('-d', '--display', action='store_true', help='Display connected ISP name')

    args = parser.parse_args()

    if args.speed:
        check_internet_speed()

    if args.ping:
        check_ping()

    if args.display:
        display_provider()

if __name__ == '__main__':
    show_banner()
    wait_time = 2.5
    wait_with_spinner(wait_time)
    main()

print(f"{Fore.GREEN}[+] Linux: {Fore.WHITE}more information About NetWork Your own Type command {Fore.RED}'{Fore.YELLOW}ip addr show{Fore.RED}' ")

print(f"{Fore.GREEN}[+] Termux: {Fore.WHITE}more information About NetWork Your own Type command {Fore.RED}'{Fore.YELLOW}ifconfig{Fore.RED}' ")
