import os
import requests
from dotenv import load_dotenv
load_dotenv()


# This class is responsible for talking to the Google Sheet.

class DataManager:

    def __init__(self):
        self.sheety_dotpoint = "https://api.sheety.co/023c1343faf9460ce2a05f29e0e609ea/flightDeals/prices"
        self.headers = {"Authorization": f"Bearer {os.getenv('api_key_sheety')}"}
        response = requests.get(url=self.sheety_dotpoint, headers=self.headers)
        # print(response.text)
        # pprint(response.json())
        self.prices = response.json()

    def updating_sheet(self, row, IATA):
        sheety_dotpoint_update = f"{self.sheety_dotpoint}/{row['id']}"
        params = {"price":
            {
                "city": f"{row['city']}",
                "iataCode": f"{IATA}",
                "lowestPrice": f"{row['lowestPrice']}"
            }
        }
        response = requests.put(url=sheety_dotpoint_update, json=params, headers=self.headers)
