from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import logging
import pandas as pd 


logging.basicConfig(level=logging.INFO, datefmt="%Y-%m-%d", format="%(levelname)s - %(asctime)s - %(message)s")

def scrape_forbes_fintech_50():
    """
    Using BS4 + requests, scrape and process HTML tags
    """
    
    url = "https://www.forbes.com/lists/fintech50/"  # Replace with the URL of the page you want to scrape
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.content
        a = SoupStrainer(name="a") # Only get all 'a' tags, more optimal than searching entire html
        soup = BeautifulSoup(html_content, "html.parser", parse_only=a) 
        data = []  # Next, look for nested div content
        for s in soup: 
            div = s.find_all('div')
            try: 
                for d in div:
                    if d == []:
                        continue
                    else:
                        str_data = next(d.strings) # Fix output 
                        data.append(str_data)
            except StopIteration as err: 
                logging.info(f'list exhaussted')
        return data
    

def process_fintech_50_records():
    """
    This function is used to process the data returned by the `scrape_forbes_fintech_50()` 
    function, which retrieves a list of strings from the Forbes Fintech 50 website.
    The function groups the strings into groups of 4 and prints each group.
    
    The function assumes that the data returned by `scrape_forbes_fintech_50()`
    will always have a length that is a multiple of 4, as the Forbes Fintech 50 list only has 4 rows.

    Returns each record grouped as a row
    """

    window = 4
    raw_data = scrape_forbes_fintech_50()
    for index in range(0, len(raw_data), window):
        if index + window <= len(raw_data):
            grouped = raw_data[index:index + window]
            return grouped
        

data = process_fintech_50_records()
df = pd.DataFrame(data)
print(df.head())