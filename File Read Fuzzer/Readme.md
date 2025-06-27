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

## ✨ Features

- 🔐 Supports Bearer Token Authorization (`-t`)
- 🧩 Three Modes of Operation:
  - `default`: Test a single file path directly
  - `filefinder`: Automatically tries `../` traversal for LFI-style discovery
  - `defaultconfig`: Bruteforces known config paths from a wordlist
- 📜 Simple and clean output with colored highlights
- 🌐 Sends `GET` requests with dynamic parameters and headers

---
