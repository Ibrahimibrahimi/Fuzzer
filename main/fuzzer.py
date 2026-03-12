import os
from .config import *
from .load import *
from .requester import *


class Fuzzer:
    def __init__(self, url: str, wordlist: str, filename=f"{HISTORY_DIR}/history_{len(os.listdir(HISTORY_DIR))}.txt"):
        self.filename = filename
        self.history = []
        self.success = []
        self.wordlist = None
        os.system("cls")
        print(LOGO)
        if get(url):
            self.url = url
            print(f"[+] URL '{url}' works well (code={code(url)})")
        else:
            print("[X] ERROR while getting from ", url)
            exit()

        if wordlist in available_wl:
            self.wordlist = wordlist
            self.lines = getLines(wordlist)
            print(f"[+] LOADED {len(self.lines)} lines from '{self.wordlist}'")

        else:
            print("[X] No wordlist found '", wordlist, "' !")
            exit()

    def start(self):
        if len(self.lines) == 0:
            print("-> Cannot start with empty wordlist")
        for line in self.lines:
            t = test(self.url, line)
            if t:
                self.success.append(line)

    def save(self):
        if len(self.success) == 0:
            print("Nothing to see (0 success)")
            return
        with open(self.filename, "w", encoding="utf-8") as history:
            for route in self.success:
                history.write(f"{route}\n")
