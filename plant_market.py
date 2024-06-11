import os
import webbrowser
import requests
import pandas as pd
from pandas import json_normalize
from utils import get_token

class PlantMarket:
    def __init__(self):
        self.browser = self.choose_browser()
        self.token = get_token()
        self.market_data = self.fetch_market_data()

    @staticmethod
    def choose_browser():
        browser_choice = input("Which browser to use? [edge/default]: ").lower()
        if browser_choice == "edge":
            return webbrowser.BackgroundBrowser(EDGE_PATH)
        return webbrowser.get()

    def fetch_market_data(self):
        headers = {
            'authorization': f'Bearer Token: {self.token}',
            # Other headers...
        }
        params = {
            'offset': '0',
            'limit': '10',
            'type': '1',
        }
        response = requests.get('https://backend-farm.plantvsundead.com/get-plants-filter-v2',
                                headers=headers, params=params)
        if response.status_code == 200:
            return json_normalize(response.json()["data"])
        else:
            print('Failed: Server did not respond')
            exit(1)

    # Other methods...
