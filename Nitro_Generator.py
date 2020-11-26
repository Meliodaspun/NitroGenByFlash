# Made By Flash
# No SKID

import random, string
import string
import os
import getpass
import webbrowser
import ctypes
from colorama import init, Fore, Back, Style
import requests
import os
import sys
import time
from colorama import Fore
import webbrowser
import ctypes

value = 0
gen = 0
ctypes.windll.kernel32.SetConsoleTitleW("Nitro Checker - Made By Flash")

os.system('cls')
print(f"""  

	  {Fore.GREEN}    ___(                        )
	  {Fore.GREEN}   (                          _)
	  {Fore.GREEN}  (_                       __))
	  {Fore.GREEN}    ((                _____)
	  {Fore.GREEN}      (_________)----'
	  {Fore.GREEN}         _/  /        {Fore.RESET}GN {Fore.GREEN}={Fore.RESET} GENERATE NITRO CODES
	  {Fore.GREEN}        /  _/
	  {Fore.GREEN}      _/  /
	  {Fore.GREEN}     / __/
	  {Fore.GREEN}   _/ /
	  {Fore.GREEN}  /__/
	  {Fore.GREEN} //         {Fore.RESET}CN {Fore.GREEN}={Fore.RESET} CHECK NITRO CODES
	  {Fore.GREEN}/'
	  {Fore.GREEN}  _____ _           _     
	  {Fore.GREEN} |  ___| | __ _ ___| |__  
	  {Fore.GREEN} | |_  | |/ _` / __| '_ \ 
	  {Fore.GREEN} |  _| | | (_| \__ \ | | |
	   |_|   |_|\__,_|___/_| |_|{Fore.RESET}
""")

chouse = input(">> ")

if chouse == "GN":
    os.system('cls')
    print(f"""  

	
	  {Fore.GREEN}    ___(                        )
	  {Fore.GREEN}   (                          _)
	  {Fore.GREEN}  (_                       __))
	  {Fore.GREEN}    ((                _____)
	  {Fore.GREEN}      (_________)----'
	  {Fore.GREEN}         _/  /    
	  {Fore.GREEN}        /  _/
	  {Fore.GREEN}      _/  /
	  {Fore.GREEN}     / __/
	  {Fore.GREEN}   _/ /
	  {Fore.GREEN}  /__/
	  {Fore.GREEN} //    
	  {Fore.GREEN}/'
	  {Fore.GREEN}  _____ _           _     
	  {Fore.GREEN} |  ___| | __ _ ___| |__  
	  {Fore.GREEN} | |_  | |/ _` / __| '_ \ 
	  {Fore.GREEN} |  _| | | (_| \__ \ | | |
	  {Fore.GREEN} |_|   |_|\__,_|___/_| |_|  {Fore.RESET}


	""")

    nitro_type = input(f"[{Fore.GREEN}>{Fore.RESET}] - Type start for start: ")

    if nitro_type == "start":
        amount = int(input(f'[{Fore.GREEN}>{Fore.RESET}] - Ammount of nitro codes to generate: '))
        value = 1
        while value <= amount:
            code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
            f = open('CODES.txt', "a+")
            f.write(f'{code}\n')
            f.close()
            value += 1
            gen += 1
            print(f'[{value}] - {code}')
            ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Checker - Made By Flash - Generate : [{gen}/{amount}]")

if chouse == "CN":
    print(f"[{Fore.GREEN}>{Fore.RESET}] - Timout: ")
    time_wait = int(input(">>> "))
    try:
        nitro = open("CODES.txt", "r").read().splitlines()
    except FileNotFoundError:
        print("The File 'CODES.txt' was not found to fix this is issue make sure the file is extracted and all the files are in the same directory.")
        time.sleep(5)
        sys.exit()
    file_hit = open("it.txt", "w")
    file_hit.close()
    non_valide = 0
    valide = 0
    for code in nitro:
        r = requests.get(f"https://discord.com/api/v7/entitlements/gift-codes/{code}")
        if r.status_code == 404:
            non_valide += 1
            print(f"{Fore.GREEN}[CHECK] |{code}| INVALID")
            ctypes.windll.kernel32.SetConsoleTitleW(
                f"Nitro Checker - Made By Flash - Codes Valides: {valide} | Codes Invalides: {non_valide}")
        elif r.status_code == 200:
            valide += 1
            file_hit = open("it.txt", "a")
            file_hit.write(f"{code}\n")
            file_hit.close()
            print(f"{Fore.GREEN}[CHECK] |{code}| VALID")
            ctypes.windll.kernel32.SetConsoleTitleW(
                f"Nitro Checker - Made By Flash - Codes Valides: {valide} | Codes Invalides: {non_valide}")
            on.system('pause')
        else:
            print("Error...")
            print(r.json())
        time.sleep(time_wait)
    print(f"{Fore.RESET}Done.")