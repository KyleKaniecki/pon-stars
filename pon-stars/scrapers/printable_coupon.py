import xmltodict
import requests
import json
from difflib import SequenceMatcher
import re
from bs4 import BeautifulSoup
import string
import time


class PrintableCouponFeedParser(object):
    """
    Works, but the site doesn't look like it's been updated in ages
    """

    def __init__(self):
        pass
    
    def parse(self):
        response = requests.get('http://printablecouponfeed.com/')

        soup = BeautifulSoup(response.content, 'html.parser')

        stores = soup.find_all('li', attrs={'itemtype': 'http://schema.org/Organization'})

        data = {}
        for store in stores:
            link = store.find('a', attrs={'itemprop': 'url'})

            store_title = link.get_text()
            link = link.get('href')

            data[store_title] = []

            response = requests.get(link)

            soup2 = BeautifulSoup(response.content, 'html.parser')

            coupons = soup2.find_all('li', attrs={'itemtype': 'http://schema.org/Offer'})

            for coupon in coupons:
                a = coupon.find('a')

                coupon_link = a.get('href')
                coupon_description = a.find('span', attrs={'itemprop': 'name'}).get_text()

                data[store_title].append({
                    'description': coupon_description,
                    'link': 'http://printablecouponfeed.com{}'.format(coupon_link)
                })
        return data