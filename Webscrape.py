import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrapeSalaries(team):
    url = f"https://www.basketball-reference.com/contracts/{team}.html"

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", id="contracts")

        if table:
            # Extract table headers
            headers = [header.text.strip() for header in table.find("thead").find_all("th")]
            headers = headers[3:]

            # Extract table rows
            rows = []
            for row in table.find("tbody").find_all("tr"):
                cells = [cell.text.strip() for cell in row.find_all(["td", "th"])]
                if cells:
                    # Remove quotation marks and commas from salary data
                    cells = [cell.replace('"', '').replace(',', '') for cell in cells]
                    rows.append(cells)

            df = pd.DataFrame(rows, columns=headers)
            return(df)

        else:
            print("No table found on the page.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}. Team: {team}")

    return None

# Example usage
# Note: Use the team abbreviations as they appear in the URL
# For example, Brooklyn Nets is "BRK" not "BKN"
arrayOfAbreviations =  ['GSW', 'LAL', 'BRK', 'MIL', 'PHO', 'DEN', 'MIA', 'BOS', 'CLE', 'CHI', 'DAL', 'HOU', 'MIN', 'OKC', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS', 'ATL', 'CHO', 'DET', 'IND', 'LAC', 'MEM', 'NOP', 'NYK', 'ORL', 'PHI']
arrayOfNames = ['Warriors', 'Lakers', 'Nets', 'Bucks', 'Suns', 'Nuggets', 'Heat', 'Celtics', 'Cavaliers', 'Bulls', 'Mavericks', 'Rockets', 'Timberwolves', 'Thunder', 'Trail Blazers', 'Kings', 'Spurs', 'Raptors', 'Jazz', 'Wizards', 'Hawks', 'Hornets', 'Pistons', 'Pacers', 'Clippers', 'Grizzlies', 'Pelicans', 'Knicks', 'Magic', '76ers']
counter = 0
for i in range(len(arrayOfAbreviations)):
    if f"{arrayOfNames[i]}Salary.csv" not in os.listdir("data"):
        df = scrapeSalaries(arrayOfAbreviations[i])
        counter += 1

        if df is not None:
            csv_filename = f"data/{arrayOfNames[i]}Salary.csv"
            print(csv_filename)
            df.to_csv(csv_filename, index=False)
        else:
            print(f"Failed to scrape salaries for {arrayOfNames[i]}")
print(counter)
check = 0
for i in range(len(arrayOfNames)):
    if f"{arrayOfNames[i]}Salary.csv" in os.listdir("data"):
        check += 1
if check == len(arrayOfNames):
    print("All salaries have been scraped")


        