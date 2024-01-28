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

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def sleep(self):
        print("zzzzzz......")

class GuardDog(Dog):

    def __init__(self, name, breed):
        super().__init__(
            name,
            breed,
            5.0,
        )
        self.aggresive = True

    def rrrrr(self):
        print("stay away!")  

class Puppy(Dog):

    def __init__(self, name, breed):
        super().__init__(
            name,
            breed,
            0.1,
        )
        self.spoiled = True

    def __str__(self):
        return f"{self.breed} puppy named {self.name}"

    def woof_woof(self):
        print("Woof Woof!")
    
ruffus = Puppy(
    name = "Ruffus",
    breed = "Beagle",
)

bibi = GuardDog(
    name = "Bibi",
    breed = "Dalmatian"
)

ruffus.sleep()
bibi.sleep()
