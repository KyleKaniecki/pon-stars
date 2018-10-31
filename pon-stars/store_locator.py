import requests
import json
from settings import WALMART_API_KEY


def find_stores(zip_code):
    """
    Finds stores in a given zip code and get the information about them
    """
    url = 'http://api.walmartlabs.com/v1/stores?apiKey={}&zip={}&format=json'.format(WALMART_API_KEY, zip_code)

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    return None