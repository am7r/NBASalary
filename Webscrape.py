import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrapeSalaries(team):
   
    return df

# Example usage
# Note: Use the team abbreviations as they appear in the URL
# For example, Brooklyn Nets is "BRK" not "BKN"
arrayOfAbreviations = ["GSW", "LAL", "BRK", "MIL", "PHO", "DEN", "MIA", "BOS", "CLE", "CHI", "DAL", "HOU", "MIN", "OKC", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]
arrayOfNames = ["Warriors", "Lakers", "Nets", "Bucks", "Suns", "Nuggets", "Heat", "Celtics", "Cavaliers", "Bulls", "Mavericks", "Rockets", "Timberwolves", "Thunder", "Trail Blazers", "Kings", "Spurs", "Raptors", "Jazz", "Wizards"]


for i in range(len(arrayOfAbreviations)):
    df = scrapeSalaries(arrayOfAbreviations[i])

    if df is not None:
        # Display the dataframe
        import ace_tools as tools; tools.display_dataframe_to_user(name=arrayOfNames[i], dataframe=df)
        # Save to CSV file
        csv_filename = f"data/{arrayOfNames[i]}Salary.csv"
        df.to_csv(csv_filename, index=False)
        
    # Add delay between requests
    time.sleep(3)  # Wait 3 seconds between requests
        
