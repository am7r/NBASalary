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
    def __init__(self, name):
        name = self.name
        players = []


def checkForMaxMin(player, averageCap):
    if player.salary/averageCap >= 0.33: # is supermax
        return 1
    elif player.salary/averageCap >= 0.23: # is max
        return 0
    elif player.salary <= 2400000.0: # is min
        return -1
    else:
        return -2
    
data = pd.read_csv("warriorsMergedData.csv")

# Create Player objects
players = []
for _, row in data.iterrows():
    player_stats = row.to_dict()  # Convert row to dictionary
    player = Player(**player_stats)  # Pass dictionary as keyword arguments
    players.append(player)

for player in players:
    print(f"--- Player: {player.Player} ---")  # Assuming 'Player' is a column in your CSV
    print(player)
    print()
