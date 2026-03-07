import requests
import colorama


def get(url: str) -> bool:
    try:
        response = requests.get(url)
        return True
    except:
        return False


def code(url: str) -> int:
    try:
        response = requests.get(url)
        return response.status_code
    except Exception as e:
        print(e)
        return 404


def test(url: str, route: str) -> str:
    Code = code(url)
    print(f"[{Code}] {url}/{route}")
    return get(url)