import os
import sys
import subprocess
import csv
import socket

def check_internet_socket():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

if check_internet_socket():
    print("There is internet access.")
else:
    print("Please check your internet connection.")

def check_requirements():
    required_packages = ['requests', 'art']
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])

check_requirements()

import requests
from art import text2art

print(text2art("TiNOS SETUP"))
print("Downloading Files...")

def main_file():
    url = 'https://xn----8sbehcec4b5afqg6e.xn--p1ai/projects/tinos/tinos.py' 
    
    target_folder = os.path.join(os.getcwd(), 'C:/TiNOS')
    filename = 'tinos.py'

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    full_path = os.path.join(target_folder, filename)

    try:       
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers, stream=True, timeout=10)

        if response.status_code == 200:
            with open(full_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print("'tinos.py' downloaded!")
        else:
            print(f"Error {response.status_code}: Server returned an error. Check if the URL is correct.")
            
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
    except PermissionError:
        print("Permission error: Try running the script as Administrator or change the target folder path.")

def wallpaper():
    url = 'https://xn----8sbehcec4b5afqg6e.xn--p1ai/projects/tinos/wallpaper.png' 
    
    target_folder = os.path.join(os.getcwd(), 'C:/TiNOS/assets')
    filename = 'wallpaper.png'

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    full_path = os.path.join(target_folder, filename)

    try:       
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        response = requests.get(url, headers=headers, stream=True, timeout=10)

        if response.status_code == 200:
            with open(full_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print("Wallpaper downloaded!")
        else:
            print(f"Error {response.status_code}: Server returned an error. Check if the URL is correct.")
            
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
    except PermissionError:
        print("Permission error: Try running the script as Administrator or change the target folder path.")

if __name__ == "__main__":
  main_file()
  wallpaper()

  os.makedirs(f"C:/TiNOS/data")
  with open("C:/TiNOS/data/users.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow("username,password")