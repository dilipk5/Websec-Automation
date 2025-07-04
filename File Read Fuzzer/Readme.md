# 🛡️ File Hunter - Config & File Discovery Tool

A Python-based automation tool to help discover sensitive files via parameter fuzzing, LFI-style traversal, and brute-force config file discovery using wordlists.

---


## 🚀 Usage

1. Deafult Mode-Use this to test for file read or LFI.
```
python main.py -u <URL> -p <param> [-f <filename>] [-w <wordlist>] [-t <token>]
```

2. Filefinder Mode - this mode recursively look for the file in the parent directories
```
python main.py --mode filefinder -u <URL> -p <param> [-f <filename>] [-t <TOKEN>]
```

3. DeafultConfig - With the help of wordlist which includes default location of config files
```
python main.py --mode defaultconfig -u <URL> -p <param> [-w <wordlist>] [-t <token>]
```
---

## EXAMPLE
1. fdbrute
```python main.py -m fdbrute -u http://api.heal.htb/download -p filename -t eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyfQ.73dLFyR_K1A7yY9uDP6xu7H1p_c7DlFQEoN1g-LFFMQ
```
2. filefinder
```
python main.py -m filefinder -u http://api.heal.htb/download -p filename -t eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyfQ.73dLFyR_K1A7yY9uDP6xu7H1p_c7DlFQEoN1g-LFFMQ -f config.php
```
3. defaultconfig
```
python main.py -m defaultconfig -u http://api.heal.htb/download -p filename -t eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyfQ.73dLFyR_K1A7yY9uDP6xu7H1p_c7DlFQEoN1g-LFFMQ -w wordlist.txt
```


---

## ✨ Features

- 🔐 Supports Bearer Token Authorization (`-t`)
- 🧩 Three Modes of Operation:
  - `default`: Test a single file path directly
  - `filefinder`: Automatically tries `../` traversal for LFI-style discovery
  - `defaultconfig`: Bruteforces known config paths from a wordlist
- 📜 Simple and clean output with colored highlights
- 🌐 Sends `GET` requests with dynamic parameters and headers

---
