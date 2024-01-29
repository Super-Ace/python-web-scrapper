class Player:

    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team

    def introduce(self):
        print(f"Hello! I'm {self.name} and I play for {self.team}")

class Team:

    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []
        
    def show_players(self):
        for player in self.players:
            player.introduce()

    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)

team_x = Team("Team X")
team_x.add_player("nico")

team_blue = Team("Team Blue")
team_blue.add_player("Lynn")

print(team_blue.show_players())