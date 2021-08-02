import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timedelta
load_dotenv()


API_KEY_KIWI = os.getenv("api_key_kiwi")


# This class is responsible for talking to the Flight Search API.


class FlightSearch:

    def __init__(self):
        self.now = datetime.now()
        sixth_month = timedelta(days=180)
        self.sixth_month_later = self.now + sixth_month


    def search_cities(self, city):

        kiwi_dotpoint = "https://tequila-api.kiwi.com/locations/query"
        kiwi_params = {
            "term": city,
            "location_types": "airport"

        }
        headers = {"apikey": API_KEY_KIWI}

        response_locations = requests.get(url=kiwi_dotpoint, params=kiwi_params, headers=headers)
        # print(response_locations)
        city_data = response_locations.json()
        iata_data = city_data["locations"][0]["id"]
        return iata_data



