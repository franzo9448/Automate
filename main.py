#!/usr/bin/env python3
import os
import time
import sys
from platform import system
from termcolor import colored
from pyfiglet import Figlet

os.system('clear')


def print_logo():
    text_logo = "Neoikiru"
    figlet = Figlet(font='slant')
    print(colored(figlet.renderText(text_logo), color="red"))


def clear_scr():
    """
    clear the screen in case of GNU/Linux or
    windows
    """
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')


def neo_exit():
    clear_scr(), sys.exit()


def menu():
    print_logo()
    print("""\033[1m
 [!] This Tool Must Run As ROOT [!] 
\033[0m
   {1}--Press here and I will do the rest
   {0}--Install / Update Neotool
   {99}-Exit
 """)
    choice = input("Neoikiru~# ")
    os.system('clear')
    if choice == "1":
        neo_install()
    elif choice == "0":
        update_neo()
    elif choice == "99":
        neo_exit()
    elif choice == "":
        menu()
    else:
        menu()


def update_neo():
    print_logo()
    print("This Tool is Only Available for Linux and Similar Systems. ")
    choice_update = input("Continue Y / N: ")
    if choice_update == "Y":
        os.system("sudo apt-get update && apt-get full-upgrade -y")
        os.system("sudo apt-get install python3-pip")
        os.system("""sudo pip3 install lolcat && sudo apt-get install -y figlet && sudo pip3 install boxes && sudo 
        apt-get install -y boxes && sudo pip3 install flask &&  sudo pip3 install requests && sudo pip3 install 
        termcolor && sudo pip3 install pyfiglet && sudo pip3 install pygments && sudo pip3 install json2html && sudo 
        pip3 install simplejson""")
        menu()
    else:
        menu()


def neo_install():
    androbugs()
    sherlock()
    red_hawk()
    nmap()
    ncrack()
    aircrack()
    hydra()
    sqlmap()
    wireshark()
    bettercap()
    autopsy()
    reconspyder()
    autopwn()
    nmap3()
    tor()
    set()
    yersinia()
    sqli()
    cruch()
    htrack()
    joomla()
    neo_exit()


def androbugs():
    print_logo()
    print("Installing Androbugs")
    os.system("git clone https://github.com/androbugs2/androbugs2.git")
    os.system("cd androbugs && pip3 install androguards && pip3 install -r requirements.txt")
    print("Installing Mongodb")
    os.system("apt-get install -y gnupg ")
    os.system("wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key -y add -")
    os.system("echo ""deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.2 main" "| sudo tee "
              "/etc/apt/sources.list.d/mongodb-org-4.2.list")
    os.system("apt-get update && apt-get install -y mongodb-org && systemctl start mongod")


def sherlock():
    print("Installing Sherlock")
    os.system("git clone https://github.com/sherlock-project/sherlock.git")
    os.system("cd sherlock && pip3 install -r requirements.txt")


def red_hawk():
    print("Installing Red Hawk")
    os.system("git clone  https://github.com/Tuhinshubhra/RED_HAWK")



def nmap():
    print("Installing Nmap")
    os.system("git clone https://github.com/nmap/nmap.git")
    os.system("cd nmap && ./configure && make && make install")


def ncrack():
    print("Installing Ncrack")
    os.system("git clone https://github.com/sophsec/ruby-ncrack.git")
    os.system("cd ruby-ncrack")
    os.system("install ruby-ncrack")


def aircrack():
    print("Installing Aircrack")
    os.system("apt-get  install -y build-essential \
                   autoconf automake libtool pkg-config \
                   libnl-3-dev libnl-genl-3-dev libssl-dev \
                   ethtool shtool rfkill zlib1g-dev libpcap-dev \
                   libsqlite3-dev libpcre3-dev libhwloc-dev libcmocka-dev\
                    hostapd wpasupplicant tcpdump screen iw usbutils")


def hydra():
    print("Installing Hydra")
    os.system("apt-get  install libssl-dev libssh-dev libidn11-dev libpcre3-dev \
                     libgtk2.0-dev libmysqlclient-dev libpq-dev libsvn-dev \
                     firebird-dev libmemcached-dev libgpg-error-dev \
                     libgcrypt11-dev libgcrypt20-dev -y")
    os.system("git clone https://github.com/vanhauser-thc/thc-hydra.git")
    os.system("cd thc-hydra")
    os.system("bash ./configure && make && make install")


def sqlmap():
    print("Installing sqlmap")
    os.system("git clone https://github.com/sqlmapproject/sqlmap.git sqlmap-dev ")


def wireshark():
    print("Installing wireshark")
    os.system("add-apt-repository  ppa:wireshark-dev/stable -y")
    os.system("apt-get update")
    os.system("apt-get -y install wireshark")


def bettercap():
    print("Installing Bettercap")
    os.system("apt install  bettercap -y")
    os.system("apt install  golang git build-essential libpcap-dev libusb-1.0-0-dev libnetfilter-queue-dev -y")
    os.system("git clone https://github.com/bettercap/bettercap")
    os.system("cd bettercap && make build")




def autopsy():
    print("Installing Autopsy")
    os.system("apt-get install autopsy  -y")


def reconspyder():
    print("Installing ReconSpider")
    os.system("git clone https://github.com/bhavsec/reconspider.git")
    os.system("apt install python3 python3-pip -y && cd reconspider && sudo pip3 install -r requirements.txt")


def autopwn():
    print("Installing AutoPWN Suite")
    os.system("pip install autopwn-suite")


def nmap3():
    print("Installing Python3-Nmap Suite")
    os.system("git clone https://github.com/wangoloj/python3-nmap.git && cd python3-nmap/")
    os.system("pip3 install -r requirements.txt")


def tor():
    print("Installo tor")
    os.system("apt-get update && apt-get install tor torbrowser-launcher -y")


def set():
    print("Installazione Social Engineer ToolKit")
    os.system("git clone https://github.com/trustedsec/social-engineer-toolkit/  && cd setoolkit")
    os.system("pip3 install -r requirements.txt && pithon3 setup.py")


def yersinia():
    print("Installazione Yrsinia")
    os.system("apt-get install yersinia  -y")


def sqli():
    print("installazione sqli")
    os.system("git clone https://github.com/raic0d3r/SQLiVulnerableScanner.git && cd SQLiVulnerableScanner && chmod +x SQLiVulnerableScanner.py ")
    os.system("pip3 install -r requirements.txt")
    os.system("apt-get install sqlmap  -y")


def htrack():
    print("installo htrack")
    os.system("git clone https://github.com/xroche/httrack.git --recurse && cd httrack")


def joomla():
    print("Installo joomla")
    os.system("git clone https://github.com/rezasp/joomscan.git && cd joomscan")


def cruch():
    print("Installo cruch")
    os.system("apt-get install crunch -y")


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(" Finishing up...\r"),
        time.sleep(0.25)
