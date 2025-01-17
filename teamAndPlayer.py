import pandas as pd

# getattr(player, '3P', 'N/A')

class NBA():
    def __init__(self, superV, mini, maxi, t1, t2, t3, t4, t5, t6):
        self.super = superV
        self.max = mini
        self.min = maxi
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6


class Player():
    def __init__(self, team, **kwargs):
        # Dynamically assign all key-value pairs as attributes
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        self.salary = float(kwargs.get('2024-25', 0))
        self.team = team
        self.tier = None

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


def segregatingContracts(team):
    cap = 140000000
    # Initialize empty lists for each salary tier
    superSal, minSal, maxSal = [], [], []
    t1, t2, t3, t4, t5, t6 = [], [], [], [], [], []

    # Salary tier thresholds
    tier_ranges = [
        (25000000, 31830356, t1, "t1"),
        (20000000, 25000000, t2, "t2"), 
        (15000000, 20000000, t3, "t3"),
        (10000000, 15000000, t4, "t4"),
        (5000000, 10000000, t5, "t5"),
        (0, 5000000, t6, "t6")
    ]

    for player in team.players:
        contract_type = checkForMaxMin(player, cap)
        
        if contract_type == 1:
            player.tier = "super"
            superSal.append(player)
        elif contract_type == 0:
            player.tier = "max"
            maxSal.append(player)
        elif contract_type == -1:
            player.tier = "min"
            minSal.append(player)
        else:
            # Categorize by salary tier
            salary = player.salary
            for low, high, tier, tier_name in tier_ranges:
                if low <= salary < high:
                    player.tier = tier_name
                    tier.append(player)
                    break

    return superSal, minSal, maxSal, t1, t2, t3, t4, t5, t6
    
        

holder = setUpTeams()
for t in holder:
    sup, minS, maxS, t1, t2, t3, t4, t5, t6 = segregatingContracts(t) # should be segregating contracts

for t in holder:
    for x in t.players:
        if x.tier == "super":
            print(x.Player, "is SuperMax")
        elif x.tier == "max":
            print(x.Player, "is Max player")
        elif x.tier == "min":
            print(x.Player, "is on a minimum")
        elif x.tier == "t1":
            print(x.Player, "is in Tier 1 ($25M-$31.8M)")
        elif x.tier == "t2":
            print(x.Player, "is in Tier 2 ($20M-$25M)")
        elif x.tier == "t3":
            print(x.Player, "is in Tier 3 ($15M-$20M)")
        elif x.tier == "t4":
            print(x.Player, "is in Tier 4 ($10M-$15M)")
        elif x.tier == "t5":
            print(x.Player, "is in Tier 5 ($5M-$10M)")
        elif x.tier == "t6":
            print(x.Player, "is in Tier 6 ($0-$5M)")
LEAGUE = NBA(sup, minS, maxS, t1, t2, t3, t4, t5, t6)
print(f"League:")
print("\nSupermax Players:")
for player in LEAGUE.super:
    print(f"- {player.Player}")

print("\nMax Contract Players:") 
for player in LEAGUE.max:
    print(f"- {player.Player}")

print("\nMinimum Contract Players:")
for player in LEAGUE.min:
    print(f"- {player.Player}")

print("\nTier 1 Players ($25M-$31.8M):")
for player in LEAGUE.t1:
    print(f"- {player.Player}")

print("\nTier 2 Players ($20M-$25M):")
for player in LEAGUE.t2:
    print(f"- {player.Player}")

print("\nTier 3 Players ($15M-$20M):")
for player in LEAGUE.t3:
    print(f"- {player.Player}")

print("\nTier 4 Players ($10M-$15M):")
for player in LEAGUE.t4:
    print(f"- {player.Player}")

print("\nTier 5 Players ($5M-$10M):")
for player in LEAGUE.t5:
    print(f"- {player.Player}")

print("\nTier 6 Players ($0-$5M):")
for player in LEAGUE.t6:
    print(f"- {player.Player}")


