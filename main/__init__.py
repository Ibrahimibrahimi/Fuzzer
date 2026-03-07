from .load import getLines
from .requester import code, get, test
import os

available_wl = os.listdir("main/wordlist")
HISTORY_DIR = "history"
if not os.path.exists(HISTORY_DIR):
    os.mkdir(HISTORY_DIR)


class Fuzzer:
    def __init__(self, url: str, wordlist: str, filename=f"{HISTORY_DIR}/history_{len(os.listdir(HISTORY_DIR))}.txt"):
        self.filename = filename
        self.history = []
        self.success = []
        self.wordlist = None
        if get(url):
            self.url = url
            print(f"URL '{url}' works well (code={code(url)})")
        else:
            print("ERROR while getting from ", url)
            exit()

        if wordlist in available_wl:
            self.wordlist = wordlist
            self.lines = getLines(wordlist)
            print(f"LOADED {len(self.lines)} lines from '{self.wordlist}'")
            exit()

        else:
            print("ERROR : no wordlist found '", wordlist, "'")
            exit()

    def start(self):
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
