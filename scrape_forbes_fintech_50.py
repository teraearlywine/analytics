from src.data_load_ops import load_df_to_source_dataset
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import re
import requests
import logging
import pandas as pd 


logging.basicConfig(level=logging.INFO, datefmt="%Y-%m-%d", format="%(levelname)s - %(asctime)s - %(message)s")


def scrape_forbes_fintech_50():
    """
        Scrapes the Forbes Fintech 50 website and returns a list 
        of strings containing the company name, industry, funding, and location
        for each company on the list.
        
        The function assumes that the data returned by the website will always
        have a length that is a multiple of 4, as the Forbes Fintech 50 list only has 4 columns.
        
        Returns:
            list: A list of strings containing the company name, 
            industry, funding, and location for each company on 
            the Forbes Fintech 50 list.
    """

    url = "https://www.forbes.com/lists/fintech50/"  # Replace with the URL of the page you want to scrape
    response = requests.get(url)
    if response.status_code == 200:
        logging.info(f"Status OKAY! Proceeding to parse HTML Content")
        html_content = response.content
        
        # Use soup strainer to only get 'a' (hyperlink) tags, optimizes bs4 process 
        # Each row in the fintech50 is a hyperlink. We can use this to zero in on the data
        # Note: This may be a cheat-mode, perhaps there's a more specific tag we can use
        # Pass as parameter to BeautifulSoup
        a = SoupStrainer(name="a") 
        soup = BeautifulSoup(html_content, "html.parser", parse_only=a) 

        # Clean data further, process nested 'div tags' in 'a tags'
        # Div tags define a section, so once we have the table isolated 
        # We can get the content within.
        data = [] 
        for s in soup: 
            div = s.find_all('div')
            try: 
                for d in div:
                    if d == []:
                        continue
                    else:
                        str_data = next(d.strings) 
                        data.append(str_data)
            # All BS4 find_all() returns is a generator object
            except StopIteration as err:        
                logging.info(f'list exhausted')
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

    raw_data = scrape_forbes_fintech_50()
    window = 4
    processed_data = []

    # Iterate over the raw data from prior function, 
    # Since the 4 columns are fixed, use range step to increment
    # in 4s
    for index in range(0, len(raw_data), window):
        if index + window <= len(raw_data):
            grouped = raw_data[index:index + window]
            processed_data.append(grouped)
    return processed_data


def construct_fintech_50_dataframe():
    """
    Final step in process, 
    Create pandas dataframe using column headers from article and processed data.
    Use to pass data to bigquery
    """
    
    columns = ['company_name', 'industry', 'funding', 'location']
    data = process_fintech_50_records()
    df = pd.DataFrame(data)
    df.columns = columns
    # Format the funding column (turn 500 m string into a numeric/int)
    rows = []
    for row in df['funding']:
        row = row.split(' ') 
        if row[1] == 'M': 
            row[0] = int(row[0])
            row[0] = row[0] * 1_000_000
        elif row[1] == 'B': 
            row[0] = float(row[0])
            row[0] = row[0] * 1_000_000_000
        row.pop()           # Removes the M + B element from each row.
        rows.append(row[0]) # Add cleaned data to empty list
    df['funding'] = rows    # Replace prior values with cleaned data
    return df

if __name__=="__main__":
    construct_fintech_50_dataframe()
    print(construct_fintech_50_dataframe())
    # Load to BigQuery
    # df = construct_fintech_50_dataframe()
    # load_df_to_source_dataset(df, 'forbes_fintech_50')