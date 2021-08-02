import os
from datetime import datetime, timedelta
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY_KIWI = os.getenv("api_key_kiwi")
MAIN_AIRPORT = "WAW"


# This class is responsible for talking to the Flight Search API.

class FlightData:

    def __init__(self):

        self.now = datetime.now()
        sixth_month = timedelta(days=180)
        self.sixth_month_later = self.now + sixth_month

    def search_flights(self, destination_city):

        kiwi_dotpoint = "https://tequila-api.kiwi.com/v2/search"
        kiwi_params = {
            "fly_from": MAIN_AIRPORT,
            "fly_to": destination_city,
            "date_from": self.now.date(),
            "date_to": self.sixth_month_later.date(),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "PLN"
        }

        headers = {"apikey": API_KEY_KIWI}

        response_flights = requests.get(url=kiwi_dotpoint, params=kiwi_params, headers=headers)
        # print(response_flights.text)
        flight_data = response_flights.json()
        return flight_data

