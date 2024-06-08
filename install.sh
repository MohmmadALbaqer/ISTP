#!/bin/bash

echo """
  _           _        _ _ 
 (_)_ __  ___| |_ __ _| | |
 | | '_ \/ __| __/ _` | | |
 | | | | \__ \ || (_| | | |
 |_|_| |_|___/\__\__,_|_|_|
                           
"""

if ! dpkg -l | grep -q python3-venv; then
  sudo apt update -qq
  sudo apt install -y python3-venv -qq
fi

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt > /dev/null 2>&1
