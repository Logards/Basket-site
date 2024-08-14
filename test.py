import requests


def all_matches():
    headers = {'Authorization': "edf0fdb8-c408-48cb-b376-968c9bf9c9d5"}
    response = requests.get("https://api.balldontlie.io/v1/games", headers=headers)
    matches = response.json()
    print(matches)


all_matches()


