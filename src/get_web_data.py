from bs4 import BeautifulSoup
from bs4 import SoupStrainer

import requests
import logging

logging.basicConfig(level=logging.INFO, datefmt="%Y-%m-%d", format="%(levelname)s - %(asctime)s - %(message)s")

url = "https://www.forbes.com/lists/fintech50/"  # Replace with the URL of the page you want to scrape
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    html_content = response.content

    a = SoupStrainer(name="a")
    soup = BeautifulSoup(html_content, "html.parser", parse_only=a) 
    
    data = []
    for s in soup: 
        div = s.find_all('div')
        for d in div:
            if d == []:
                pass 
            else: 
                str_data = list(d.strings) # Fix output 
                data.append(str_data)
    print(data)