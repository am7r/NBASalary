import pandas as pd

# getattr(player, '3P', 'N/A')

class Player():
    def __init__(self, **kwargs):
        # Dynamically assign all key-value pairs as attributes
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        self.salary = float(kwargs.get('2024-25', 0))

    def __str__(self):
        # Print all attributes in a single line
        attributes = vars(self)  # or self.__dict__
        return ", ".join(f"{key}: {value}" for key, value in attributes.items())

    def __repr__(self):
        return self.__str__()

class Team():

    def __init__(self, teamName, totalSalary, playersArr):
        self.name = teamName
        self.players = playersArr
        self.cap = totalSalary


def checkForMaxMin(player, averageCap):
    if player.salary/averageCap >= 0.33: # is supermax
        return 1
    elif player.salary/averageCap >= 0.23: # is max
        return 0
    elif player.salary <= 2400000.0: # is min
        return -1
    else:
        return -2
    


teamsFinal = ['Blazers', 'Bucks', 'Bulls', 'Cavaliers', 'Celtics', 'Clippers', 'Grizzlies', 'Hawks', 'Heat', 'Hornets', 'Jazz', 'Kings', 'Knicks', 'Lakers', 'Magic', 'Mavericks', 'Nets', 'Nuggets', 'Pacers', 'Pelicans', 'Pistons', 'Raptors', 'Rockets', 'Spurs', 'Suns', 'Thunder', 'Wolves', 'Warriors', 'Wizards', 'Sixers']
teamsTest = ["Warriors"]
teams = []
for team in teamsTest: # need to be changed later
    fileName = f"data/{team}MergedData.csv"
    data = pd.read_csv(fileName)

    players = []
    totalSal = 0

    for _, row in data.iterrows():
        player_stats = row.to_dict()  # Convert row to dictionary
        player = Player(**player_stats)  # Pass dictionary as keyword arguments
        players.append(player)
        if player.salary != "":  
            totalSal += player.salary

    currTeam = Team(team, totalSal, players)
    teams.append(currTeam)

    # printer function to test (not needed)

for t in teams:
    print(t.name)
    for p in t.players:
        print(p.Player)
        print()
    print(t.cap)
