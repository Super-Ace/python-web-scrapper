def create_player_for_team(name, xp, team):
    pass

def create_player(name, xp, team):
    return {
    "name": name,
    "XP": xp,
    "team": team
    }

def introduct_player(player):
    name = player["name"]
    team = player["team"]
    print(f"Hello! My name is {name} and I play for {team}")

# introduct_player(1212)

nico = create_player("Nico", 1500, "Team X")
lynn = create_player("Lynn", 1500, "Team Blue")

teams = {
    "Team X": [nico],
    "Team Blue" : [lynn]
}

class Puppy:

    def __init__(self):
        self.name = "Ruffus"
        self.age = 0.1
        self.breed = "Beagle"
    
ruffus = Puppy()
bibi = Puppy()

print(
    ruffus.name,
    ruffus.age, 
    ruffus.breed,
    )