import requests


BASE_URL = "https://uapis.cn/api/v1/dictionary/lookup"


def lookup_word(word):
    url = f"{BASE_URL}?word={word}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()