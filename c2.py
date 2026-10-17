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

# proxies.txt ফাইল না থাকলে যেন এরর না দেয়, তার ব্যবস্থা
try:
    proxys = open('proxies.txt').readlines()
    bots = len(proxys)
except:
    bots = 0

def ascii_vro():
    clear()
    print('''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  
    ''')
    time.sleep(0.4)
    clear()

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
        if cnc in ["layer7", "LAYER7", "L7", "l7"]:
            layer7()
        elif cnc in ["layer4", "LAYER4", "L4", "l4"]:
            layer4()
        elif cnc in ["amp", "AMP", "amps/games"]:
            amp_games()
        elif cnc in ["special", "SPECIAL"]:
            special()
        elif cnc in ["rules", "RULES"]:
            rules()
        elif cnc in ["clear", "CLEAR", "cls"]:
            main()
        elif cnc in ["ports", "PORTS"]:
            ports()
        elif cnc in ["tools", "TOOLS"]:
            tools()
        elif cnc in ["banner", "BANNERS"]:
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
