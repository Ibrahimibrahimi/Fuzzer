# the main executable file


from main import Fuzzer


fuzzer = Fuzzer(
    url="https://maths-france.fr/"
)

fuzzer.start()

fuzzer.save()
