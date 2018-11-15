import xmltodict
import requests
import json
from difflib import SequenceMatcher
import re
from bs4 import BeautifulSoup
import string
import time


class CouponSurferFeedParser(object):
    """
    Works, but doesn't specify a store. Will need to figure that out manually
    """

    def __init__(self):
        pass
    
    def parse(self):
        response = requests.get('https://www.couponsurfer.com/rss2.xml')

        blob = xmltodict.parse(response.content)

        coupons = blob['rss']['channel']['item']
        
        coupons = [{'description': coupon['description'], 'link': coupon['link'], 'date': coupon['pubDate']}
        for coupon in coupons]
        
        return coupons