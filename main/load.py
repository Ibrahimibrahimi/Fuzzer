import os


def getLines(path: str) -> list[str]:
    if not os.path.exists(f"main/wordlist/{path}"):
        print(f"{path} DOESNT EXIST", "Verify it is in the wordlist folder")
        exit()
    # load
    with open(f"main/wordlist/{path}", "r") as wl:
        return [i.strip() for i in wl.readlines()]
