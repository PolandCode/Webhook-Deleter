# Modules importation
import time
import os
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
try:
    import requests
except:
    os.system("py -m pip instamm requests")
    import requests

init()
os.system("title 𝗪𝗘𝗕𝗛𝗢𝗢𝗞 𝗗𝗘𝗟𝗘𝗧𝗘𝗥")
banner = (Fore.YELLOW + """

POLAND WAS HERE
POLAND WAS HERE
                                                                                                                    
""" + Fore.LIGHTCYAN_EX)
print(banner)
webhook = input(" [INPUT] ENTER UR WEBHOOK LINK lol: ")

def delete():
    requests.delete(webhook)
    check = requests.get(webhook)
    if check.status_code == 404:
        print("\n [LOGS] WEBHOOK SUPRIMMER")
        os.system("pause >nul")  # Pause command in Batch (appuyer sur une touche pour quitter)
    elif check.status_code == 200:
        print("\n [LOGS] WEBHOOK NON SUPPRIMER")
        os.system("pause >nul")

test = requests.get(webhook)
if test.status_code == 404:
    print("\n [LOGS] WEBHOOK INVALIDE")
    os.system("pause >nul")
elif test.status_code == 200:
    print("\n [LOGS] WEBHOOK VALIDE")
    delete()