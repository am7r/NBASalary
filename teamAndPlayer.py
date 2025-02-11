import pandas as pd
import testing

# getattr(player, '3P', 'N/A')

# Constants for NBA salary caps and thresholds
NBA_SALARY_CAP = 140000000
SUPERMAX_THRESHOLD = 0.33  # 33% of cap
MAX_THRESHOLD = 0.23      # 23% of cap

# Minimum salary table based on years of experience
MIN_SALARY_TABLE = {
    0: 1157153,  # Rookie
    1: 1862265,
    2: 2087519,
    3: 2162606,
    4: 2237691,
    5: 2425403,
    6: 2613120,
    7: 2800834,
    8: 2988550,
    9: 3003427,
    10: 3303771  # 10+ years
}

# Salary tier definitions (low, high, tier_name)
TIER_RANGES = [
    (25000000, 31830356, "t1"),
    (20000000, 25000000, "t2"),
    (15000000, 20000000, "t3"),
    (10000000, 15000000, "t4"),
    (5000000, 10000000, "t5"),
    (0, 5000000, "t6")
]

class NBA():
    def __init__(self, superV, mini, maxi, t1, t2, t3, t4, t5, t6, pg, sg, sf, pf, center):
        self.super = superV
        self.min = mini
        self.max = maxi
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.t4 = t4
        self.t5 = t5
        self.t6 = t6
        self.pg = pg 
        self.sg = sg 
        self.sf = sf 
        self.pf = pf 
        self.center = center


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
    if player.salary/averageCap >= SUPERMAX_THRESHOLD:  # is supermax
        return 1
    elif player.salary/averageCap >= MAX_THRESHOLD:  # is max
        return 0
    else:
        exp = player.Exp + 1
        min_salary = MIN_SALARY_TABLE[10] if exp >= 10 else MIN_SALARY_TABLE.get(exp, 0)
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
    # Initialize empty lists for each salary tier
    superSal, minSal, maxSal = [], [], []
    t1, t2, t3, t4, t5, t6 = [], [], [], [], [], []
    pg, sg, sf, pf, center = [], [], [], [], []
    tier_lists = {"t1": t1, "t2": t2, "t3": t3, "t4": t4, "t5": t5, "t6": t6}

    for player in team.players:
        contract_type = checkForMaxMin(player, NBA_SALARY_CAP)
        
        # Categorize by position
        pos = player.Pos_x
        if pos == 'PG':
            pg.append(player)
        elif pos == 'SG':
            sg.append(player)
        elif pos == 'SF':
            sf.append(player)
        elif pos == 'PF':
            pf.append(player)
        elif pos == 'C':
            center.append(player)
        
        # Categorize by salary tier
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
            salary = player.salary
            for low, high, tier_name in TIER_RANGES:
                if low <= salary < high:
                    player.tier = tier_name
                    tier_lists[tier_name].append(player)
                    break

    return superSal, minSal, maxSal, t1, t2, t3, t4, t5, t6, pg, sg, sf, pf, center
    

def calculateAverages(tier, stat):
    if not tier:  # Handle empty tier case
        return 0
    length = len(tier)
    val = 0
    for p in tier:
        val += getattr(p, stat, 0)
    return val / length

def calculateStandardDeviation(tier, stat):
    if not tier:  # Handle empty tier case
        return 0
        
    # Calculate mean first
    mean = calculateAverages(tier, stat)
    
    # Calculate sum of squared differences
    squared_diff_sum = 0
    for player in tier:
        squared_diff_sum += (getattr(player, stat, 0) - mean) ** 2
        
    # Calculate variance and standard deviation
    variance = squared_diff_sum / len(tier)
    std_dev = variance ** 0.5
    
    return std_dev



holder = setUpTeams()
for t in holder:
    sup, minS, maxS, t1, t2, t3, t4, t5, t6, pg, sg, sf, pf, center = segregatingContracts(t) # should be segregating contracts

LEAGUE = NBA(sup, minS, maxS, t1, t2, t3, t4, t5, t6, pg, sg, sf, pf, center)
testing.test(LEAGUE)
print(calculateStandardDeviation(t5, "PTS"))