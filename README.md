# Elections scraping 
Let's use an LLM to create a scraper for the Massachusetts state electios website.

## Setup

### Set up your project environment
1. First, clone this repo
2. Set up your python virtual environment
    1. Just in case your virtual environemnt from yesterday is still active, run `deactivate`. If doing so gives you an error, don't worry!
    2. Create a new Python virtual environment: 
        ```sh
        python3 -m venv scrape_env
        ```
    3. Activate the new virtual environment: 
        ```sh 
        source ./scrape_env/bin/activate 
        ```
    4. Install the `lxml`, `requests`, and `BeautifulSoup` python libraries:
        ```sh
        pip install lxml requests beautifulsoup4
        ```

### Task instructions
1. Visit the website: https://electionstats.state.ma.us/elections/search/year_from:2025/year_to:2025
2. Check `robots.txt` file (visit https://electionstats.state.ma.us/robots.txt). What preferences does this site express about whether they want to be scraped or not?
3. Inspect the page to identify the table where election data is stored:
    a. Right-click anywhere on the page > Click "Inspect" > find the table with election data
4. Read the IMDB scraper example to scrape the elections website and discuss what each line does with your teammate.
5. Make a new scraper in `election-scraper.py` that scrapes information from the MA state gov website. Complete the following tasks by copy/paste and modifying lines from the IMDB scraper code one-by-one.

    a. Task 1: grab each row of the table (What is the CSS Selector for this?)
    b. Task 2: extract the year and print it out
    b. Task 3: extract the name of the candidate and print it out
    c. Task 4: extract the name of the party and print it out

5. Ask the LLM to help you write the code to save the data to a CSV file.
6. Adjust your scraper to only grab 2024 elections. Hint: try manually adjusting the the year filters on the elections website. Does the URL change? 
7. Bonus: Extract additional data fields!
