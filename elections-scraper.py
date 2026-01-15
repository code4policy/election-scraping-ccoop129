# Copy/paste the code from the IMDB scraper ONE LINE AT A TIME
#
# When you paste the line, review what it does and modify it to 
# scrape this elections website instead of IMDB

import requests
url = "https://electionstats.state.ma.us/elections/search/year_from:2024/year_to:2025"

# get the page
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(url, headers=headers)

# extract HTML as structured "soup"
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# get each row of the table (what is the css selector for the whole row?)
elections = soup.select("tr.election_item")


# Loop through the rows and extract the year
for election in elections:
    year = election.select_one("td.year").text.strip()
    print(year)