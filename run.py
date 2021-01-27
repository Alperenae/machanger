#!\bin\pyhton3 

import os
import time

# COLORS
G = '\033[1;34m[*] \033[0m'
S = '\033[1;32m[+] \033[0m'
W = '\033[1;33m[!] \033[0m' 
OKGREEN = '\033[92m'
FAIL = '\033[91m'
WARNING = '\033[93m'

# BANNER
print("\n░M░A░C░C░H░A░N░G░E░R░")

# CODE 
print("\n" + WARNING + S +"For quite ctrl+c/z")
time.sleep(1)
show_log = True
while show_log:
    print(OKGREEN + "\nYour Current MAC Adress " + G + "\n")
    os.system("macchanger --show eth0")

    print(FAIL + "\nYour MAC Adress Changed " + W + "\n")
    os.system("macchanger -a eth0")
    
    time.sleep(10)