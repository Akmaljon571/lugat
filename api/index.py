import requests


def API(text):
    url = "https://translated-mymemory---translation-memory.p.rapidapi.com/get"

    querystring = {"langpair": "uz|ru", "q": text, "mt": "1", "onlyprivate": "0", "de": "a@b.c"}

    headers = {
        "X-RapidAPI-Key": "d2b9d8f0a5msha218323a46e63fap19b7bbjsnffa38f77c205",
        "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()
