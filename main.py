from IATA_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from pprint import pprint

flight_search = FlightSearch()
data_manager = DataManager()
print(data_manager.prices)

for IATA in data_manager.prices["prices"]:
    if IATA["iataCode"] == "":
        print(f"{IATA} iata is empty")
        iata_city = flight_search.search_cities(IATA["city"])
        data_manager.updating_sheet(IATA, iata_city)

flight_data = FlightData()

print(f"The lowest price: ")
for IATA in data_manager.prices["prices"]:
    current_flight = flight_data.search_flights(IATA["iataCode"])

    try:
        current_flight_formatted = current_flight['data'][0]
        data_from = current_flight_formatted['route'][0]['local_departure'].split("T")
        data_to = current_flight_formatted['route'][1]['local_departure'].split("T")
        print(f"From: {current_flight_formatted['cityFrom']}-{current_flight_formatted['flyFrom']}  "
              f"To: {current_flight_formatted['cityTo']}-{current_flight_formatted['flyTo']} "
              f"price: {current_flight_formatted['price']} PLN"
              f",from {data_from[0]} to {data_to[0]}")

    except:
        pass

    finally:
        print("\n")
