nico = {
    "name": "Nico",
    "XP": 1000,
    "team": "Team X"
}

def introduct_player(player):
    name = player["name"]
    team = player["team"]
    print(f"Hello! My name is {name} and I play for {team}")

introduct_player(nico)
