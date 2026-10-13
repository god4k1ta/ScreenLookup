import requests

BASE_URL = "http://127.0.0.1:5000/translate"


def translation_text(source_text):
    response = requests.post(
        BASE_URL,
        json={
            "q": source_text,
            "source": "auto",
            "target": "ru",
            "format": "text",
            "alternatives": 3
        },
        timeout=10
    )
    response.raise_for_status()
    translation = response.json()
    return translation
