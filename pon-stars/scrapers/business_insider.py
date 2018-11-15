import xmltodict
import requests
import json
from difflib import SequenceMatcher
import re
from bs4 import BeautifulSoup
import string
import time


class BusinessInsiderParser(object):
    """
    Works but against TOS
    """

    def __init__(self):
        pass
    
    def parse(self):
        response = requests.get('https://coupons.businessinsider.com/stores', timeout=15)
        soup = BeautifulSoup(response.content, 'html.parser')
        letters = soup.find_all('ul', attrs={'class': 'businessinsiderus-retailers-alphabet-sublist'})

        stores = []
        for letter in letters:
            stores += letter.find_all('li')

        store_data = []
        for store in stores:
            link = store.find('a')
            store_data.append({
                'title': link.get_text().strip(),
                'link': 'https://coupons.businessinsider.com{}'.format(link.get('href'))
            })

            coupons = self.get_coupons_from_store({
                'title': link.get_text().strip(),
                'link': 'https://coupons.businessinsider.com{}'.format(link.get('href'))
            })

            break
        
        return store_data
    
    def get_coupons_from_store(self, store: dict):
        response = requests.get(store['link'])

        soup = BeautifulSoup(response.content, 'html.parser')

        coupons = soup.find_all('div', attrs={'class': 'businessinsiderus-voucher'})

        for coupon in coupons:
            deal = coupon.find('div', attrs={'class': 'businessinsiderus-voucher-left-wrapper'}).get_text()

            print(deal.strip())

            try:
                title = coupon.find('h3', attrs={'class': 'businessinsiderus-voucher-title'}).get_text()
                print(title.strip())
            except AttributeError:
                title = coupon.find('div', attrs={'class': 'businessinsiderus-voucher-title'}).get_text()
                print(title.strip())