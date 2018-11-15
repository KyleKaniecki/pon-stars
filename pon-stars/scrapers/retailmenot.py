import xmltodict
import requests
import json
from difflib import SequenceMatcher
import re
from bs4 import BeautifulSoup
import string
import time


class RetailMeNotParser(object):
    """
    Does not work, probably because they try to prevent scraping
    """

    def __init__(self):
        pass
    
    def parse(self):
        letters = list(string.ascii_uppercase)

        store_data = []
        for letter in letters:
            response = requests.get('https://www.retailmenot.com/sitemap/{}'.format(letter), timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')

            stores = soup.find('ul', attrs={'class': 'seomap-list'}).find_all('li')

            for store in stores:
                link = store.find('a')

                store_data.append({
                    'title': link.get_text(),
                    'link': link.get('href')
                })
            
            print(store_data)
            time.sleep(1)
        return store_data