# the main executable file


from main import Fuzzer


fuzzer = Fuzzer(
    url="https://www.google.com",
    wordlist="wordpress.txt"
)

fuzzer.start()

fuzzer.save()