import os

# COLORS
S = '\033[1;32m[+] \033[0m'
W = '\033[1;33m[!] \033[0m'
ENDC = '\033[0m'

print("\n" + W + "\033[1;35;1mRequired Applications Downloading\n" + ENDC)
 
os.system("apt-get update")
os.system("apt-get -y install macchanger")
os.system("apt-get -y install python3")

print("\n" + S + "Downloading Done...")