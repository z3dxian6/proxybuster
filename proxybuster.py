#!/usr/bin/env python3
import requests
from urllib.parse import urljoin
import sys

# ANSI colors
GREEN = '\033[92m'
YELLOW = '\033[93m'
ORANGE = '\033[33m'
PURPLE = '\033[95m'
RESET = '\033[0m'

# Target settings
target = "http://172.16.1.13/"  # Change this as needed
wordlist = "/usr/share/wordlists/dirb/common.txt"
max_depth = 3  # Maximum recursion depth

session = requests.Session()
session.verify = False
session.timeout = 5

visited = set()

def enumerate_path(base_url, depth):
    if depth > max_depth or base_url in visited:
        return
    visited.add(base_url)

    print(f"[+] Scan: {base_url} (depth {depth})")

    try:
        with open(wordlist, "r") as f:
            for line in f:
                word = line.strip()
                url = urljoin(base_url, word)
                try:
                    response = session.get(url)
                    code = response.status_code

                    # Color based on code
                    if code == 200:
                        color = GREEN
                    elif 301 <= code <= 308:
                        color = YELLOW
                    elif 400 <= code <= 430:
                        color = ORANGE
                    elif 500 <= code <= 511:
                        color = PURPLE
                    else:
                        continue  # Ignore others

                    print(f"{color}[{code}] {url}{RESET}")

                    # Recurse only if the URL ends with "/" and returns a 200 status code
                    if code == 200 and url.endswith("/"):
                        enumerate_path(url, depth + 1)
                except Exception:
                    continue
    except FileNotFoundError:
        print("[-] Wordlist not found:", wordlist)
        sys.exit(1)

# Start enumeration
print(f"[+] Lancement de l'énumération sur : {target}\n")
enumerate_path(target, 1)
print("[+] Scan terminé.")
