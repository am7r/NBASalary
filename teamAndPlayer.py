import pandas as pd

# getattr(player, '3P', 'N/A')

class NBA():
    def __init__(self, super, min, max):
        self.super = super
        self.max = min
        self.min = max


class Player():
    def __init__(self, team, **kwargs):
        # Dynamically assign all key-value pairs as attributes
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        self.salary = float(kwargs.get('2024-25', 0))
        self.team = team
        self.isSuper = False
        self.isMax = False
        self.isMin = False

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
    min_salary_table = {
        0: 1157153,
        1: 1862265,
        2: 2087519,
        3: 2162606,
        4: 2237691,
        5: 2425403,
        6: 2613120,
        7: 2800834,
        8: 2988550,
        9: 3003427,
        10: 3303771  
    }

    if player.salary/averageCap >= 0.33: # is supermax
        return 1
    elif player.salary/averageCap >= 0.23: # is max
        return 0
    else:
        exp = player.Exp + 1
        min_salary = min_salary_table[10] if exp >= 10 else min_salary_table.get(exp, 0)
        if player.salary <= min_salary:
            return -1
        return -2
    

def setUpTeams():
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
            player = Player(team, **player_stats)  # Pass dictionary as keyword arguments
            players.append(player)
            if player.salary != "":  
                totalSal += player.salary
        
        currTeam = Team(team, totalSal, players)

        teams.append(currTeam)
    return teams

def setUpMax(team):
    cap = 140000000
    superSal = minSal = maxSal = []
    for p in team.players:
        temp = checkForMaxMin(p, cap)
        if temp == 1:
            p.isSuper = True
            superSal.append(p)
        if temp == 0:
            p.isMax = True
            maxSal.append(p)
        if temp == -1:
            p.isMin = True
            minSal.append(p)
    return superSal, minSal, maxSal
        

holder = setUpTeams()
for t in holder:
    sup, minS, maxS = setUpMax(t)

for t in holder:
    for x in t.players:
        if x.isSuper:
            print(x.Player, "is SuperMax")
        elif x.isMax:
            print(x.Player, "is Max player")
        elif x.isMin:
            print(x.Player, "is on a minimum")
            print(x.salary)
print(holder[0].cap)
LEAGUE = NBA(sup, minS, maxS)

