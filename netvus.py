from requests import Session
from colorama import Fore,Style
from os import system as cmd
from bs4 import BeautifulSoup as BS
import argparse
import sys
import nmap
import socket

s = Session()
p = nmap.PortScanner()

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='Target IP/Domain')
parser.add_argument('-s', '--search', help='Search Exploit ID')
args = parser.parse_args()

def banner(target):
    cmd('clear')
    print(f'''{Style.BRIGHT}
    {Fore.RED},    ,    {Fore.BLUE}/\   /\\
   /( /\ )\  _\ \_/ /_
   |\_||_/| < \_   _/ >
   \______/  \|{Fore.RED}0   0{Fore.BLUE}|/
     _\/_   _(_  ^  _)_
    (_()_) /\| {Fore.WHITE}V"""V{Fore.BLUE}|/\\
      ||   \  \_____/  /
      ||   /\   )=(   /\\
      []  /  \_/\=/\_/  \\
-----------|   ABOUT   |-----------{Fore.WHITE}
 SCRIPT    : Network Scanner V0.2
 TARGET    : {target}
 AUTHOR    : Gh05t666nero
 WEBSITE   : Deepweb.id
{Fore.BLUE}-----------|   TOOLS   |-----------''')

def scanning(host):
    banner(args.target)
    scan = p.scan(host,'0-1000')
    port = list(scan['scan'][host]['tcp'].keys())
    for tekno in port:
        product = scan['scan'][host]['tcp'][tekno]['product']
        version = scan['scan'][host]['tcp'][tekno]['version']
        outputs = f'{product} {version.strip()}'
        if outputs == ' ' or outputs == '':
            continue
        else:
            headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:93.0) Gecko/20100101 Firefox/93.0'}
            tenable = 'https://www.tenable.com/_next/data/B307Ei_yBxIgZ9c_Tg6vU/en/plugins/search.json?q='+outputs
            request = s.get(tenable, headers=headers).json()

            if "errorMessage" in request:
                sys.exit(f"{Fore.RED}ERROR KETIKA MENGIDENTIFIKASI KERENTANAN")
            else:
                print(f'\n{Fore.BLUE}[!] PORT {Fore.WHITE}{tekno} ({outputs}){Fore.BLUE} TERPAPAR CVE!')
                plugins = request['pageProps']['plugins']
                for plugin in plugins:
                    desc = plugin['_source']['description'].split(' ')
                    scid = plugin['_source']['script_id']
                    name = plugin['_source']['script_name']
                    words = outputs.split(' ')
                    if any(words[0] in word for word in desc) and any(words[1] in word for word in desc):
                        print(f'''{Fore.RED}             [{scid}] {name}''')
                        break

def searching(exploit_id):
    banner(args.search)
    api_link = 'https://www.tenable.com/plugins/nessus/'+exploit_id
    api_data = s.get(api_link).text

    soup = BS(api_data, 'html.parser')
    refe = soup.find_all('section', {'class':'mb-3'})[3].find_all('a')

    print(f'''{Fore.WHITE}
#############################################################
# TITLE   : {soup.find('meta', {'property':'og:title'})['content'].title()}
# SEVERITY: {soup.find('span', {'class':'badge badge-critical'}).text.title()}
# SYNOPSYS: {soup.find('meta', {'name':'description'})['content']}

#############################################################
[*] DESCRIPTION:
=================
{soup.find_all('section', {'class':'mb-3'})[1].find('span').text}

#############################################################
[*] REMEDIATION:
=================
{soup.find_all('section', {'class':'mb-3'})[2].find('span').text}

#############################################################
[*] REFERENCE:
===============''')
    for link in refe:
        link = print(link['href'])


if args.target is not None and args.search is None:
    scanning(args.target)
elif args.search is not None and args.target is None:
    searching(args.search)
else:
    sys.exit(f"{Fore.RED}{Style.BRIGHT}MOHON UNTUK MEMASUKKAN SATU ARGUMEN SAJA!")