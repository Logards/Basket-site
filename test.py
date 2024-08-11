import requests


def all_players():
    headers = {'Authorization': "edf0fdb8-c408-48cb-b376-968c9bf9c9d5"}
    response = requests.get("https://api.balldontlie.io/v1/players", headers=headers)
    players = response.json()
    for player in players['data']:
        print(player['first_name'], player['last_name'])


def all_teams():
    headers = {'Authorization': "edf0fdb8-c408-48cb-b376-968c9bf9c9d5"}
    response = requests.get("https://api.balldontlie.io/v1/teams", headers=headers)
    teams = response.json()
    for team in teams['data']:
        if team["conference"] == '    ':
            team["conference"] = "No information about conference"
        if team["division"] == "":
            team["division"] = "No information about division"
        if team["city"] == "":
            team["city"] = "No information about city"
    return teams


print(all_teams())
