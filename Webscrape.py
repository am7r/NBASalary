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
                    cells = [cell.replace('"', '').replace(',', '') for cell in cells]
                    rows.append(cells)

            df = pd.DataFrame(rows, columns=headers)
            return(df)

        else:
            print("No table found on the page.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}. Team: {team}")

    return None


def scrapePerGame(team):
    url = f"https://www.basketball-reference.com/teams/{team}/2025.html"

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", id="per_game_stats")

        if table:
            headers = [header.text.strip() for header in table.find("thead").find_all("th")]
            #headers = headers[]

            rows = []
            for row in table.find("tbody").find_all("tr"):
                cells = [cell.text.strip() for cell in row.find_all(["td", "th"])]
                if cells:
                    rows.append(cells)

            df = pd.DataFrame(rows, columns=headers)
            return(df)
        else:
            print("No table found on the page.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}. Team: {team}")

    return None

def scrapeColleges(team):
    url = f"https://www.basketball-reference.com/teams/{team}/2025.html"

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", id="roster")

        if table:
                headers = [header.text.strip() for header in table.find("thead").find_all("th")]
                #headers = headers[]

                rows = []
                for row in table.find("tbody").find_all("tr"):
                    cells = [cell.text.strip() for cell in row.find_all(["td", "th"])]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                return(df)
        else:
            print("No table found on the page.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}. Team: {team}")

    return None

def check(arrayOfNames):
    checkSalaries(arrayOfNames)
    checkPerGame(arrayOfNames)

def checkSalaries(arrayOfNames):
    check = 0
    for i in range(len(arrayOfNames)):
        if f"{arrayOfNames[i]}Salary.csv" in os.listdir(f"data/{arrayOfNames[i]}"):
            check += 1
    if check == len(arrayOfNames):
        print("All salaries have been scraped")
    else:
        print(f"Only {check} salaries have been scraped")

def checkPerGame(arrayOfNames):
    check = 0
    for i in range(len(arrayOfNames)):
        if f"{arrayOfNames[i]}1.csv" in os.listdir(f"data/{arrayOfNames[i]}"):
            check += 1
    if check == len(arrayOfNames):
        print("All per game stats have been scraped")
    else:
        print(f"Only {check} per game stats have been scraped")

def scrape(arrayOfNames, arrayOfAbreviations, file):
    if not os.path.exists(f"data/{arrayOfNames[i]}"):
        os.makedirs(f"data/{arrayOfNames[i]}")
    df = None
    check = False
    if f"{arrayOfNames[i]}{file}.csv" not in os.listdir(f"data/{arrayOfNames[i]}"):
        check = True
        if file == "Salary":
            df = scrapeSalaries(arrayOfAbreviations[i])
        elif file == "1":
            df = scrapePerGame(arrayOfAbreviations[i])
        elif file == "3":
            df = scrapeColleges(arrayOfAbreviations[i])

    if df is not None:
        csv_filename = f"data/{arrayOfNames[i]}/{arrayOfNames[i]}{file}.csv"
        print(csv_filename)
        df.to_csv(csv_filename, index=False)
    elif not check:
        print(f"file {file} for {arrayOfNames[i]} already scraped")
    else:
        print(f"error with {file} for {arrayOfNames[i]}")




arrayOfAbreviations =  ['GSW', 'LAL', 'BRK', 'MIL', 'PHO', 'DEN', 'MIA', 'BOS', 'CLE', 'CHI', 'DAL', 'HOU', 'MIN', 'OKC', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS', 'ATL', 'CHO', 'DET', 'IND', 'LAC', 'MEM', 'NOP', 'NYK', 'ORL', 'PHI']
arrayOfNames = ['Warriors', 'Lakers', 'Nets', 'Bucks', 'Suns', 'Nuggets', 'Heat', 'Celtics', 'Cavaliers', 'Bulls', 'Mavericks', 'Rockets', 'Timberwolves', 'Thunder', 'Trail Blazers', 'Kings', 'Spurs', 'Raptors', 'Jazz', 'Wizards', 'Hawks', 'Hornets', 'Pistons', 'Pacers', 'Clippers', 'Grizzlies', 'Pelicans', 'Knicks', 'Magic', '76ers']
counter = 0

for i in range(len(arrayOfAbreviations)):
    scrape(arrayOfNames, arrayOfAbreviations, "Salary")
    #scrape(arrayOfNames, arrayOfAbreviations, "1")
    #scrape(arrayOfNames, arrayOfAbreviations, "3")
    #scrape(arrayOfNames, arrayOfAbreviations, "3")
    

check(arrayOfNames)

        