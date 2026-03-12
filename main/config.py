import os


HISTORY_DIR = "main/history"
available_wl = os.listdir("main/wordlist")
if not os.path.exists(HISTORY_DIR):
    os.mkdir(HISTORY_DIR)


LOGO = """\
 __________________________________________________ 
|    ,------.                                      |
|    |  .---',--.,--.,-----.,-----. ,---. ,--.--.  |
|    |  `--, |  ||  |`-.  / `-.  / | .-. :|  .--'  | 
|    |  |`   '  ''  ' /  `-. /  `-.\   --.|  |     |
|    `--'     `----' `-----'`-----' `----'`--'     |
|__________________________________________________|
"""


def makeUserChooseWordlist() -> str:
    ws = os.listdir("main/wordlist")
    a = None
    while a == None or a in ws:
        print("------ Wordlists ------ ")
        for i in range(len(ws)) :
            print(f"[{i+1}] {ws[i]}")
        a = int(input("choice : "))
        if a in range(1,len(ws)+1) :
            return ws[a]
        print("Please choose number from the list")
    