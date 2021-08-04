from IATA_search import FlightIATA
from data_manager import DataManager
from flight_data import FlightData
from pprint import pprint

flight_iata = FlightIATA()
data_manager = DataManager()
print(data_manager.prices)

for IATA in data_manager.prices["prices"]:
    if IATA["iataCode"] == "":
        print(f"{IATA} iata is empty")
        iata_city = flight_iata.search_cities(IATA["city"])
        data_manager.updating_sheet(IATA, iata_city)

flight_data = FlightData()

print(f"The lowest price: ")
for IATA in data_manager.prices["prices"]:
    current_flight = flight_data.search_flights(IATA["iataCode"])

    if current_flight is None:
        continue
    else:
        try:

            current_flight_formatted = current_flight
            data_from = current_flight_formatted['route'][0]['local_departure'].split("T")
            data_to = current_flight_formatted['route'][1]['local_departure'].split("T")
            print(f"From: {current_flight_formatted['cityFrom']}-{current_flight_formatted['flyFrom']}  "
                  f"To: {current_flight_formatted['cityTo']}-{current_flight_formatted['flyTo']} "
                  f"price: {current_flight_formatted['price']} PLN"
                  f",from {data_from[0]} to {data_to[0]}")

            if flight_data.kiwi_params["max_stopovers"] > 0:
                print(current_flight_formatted)
                print(f"\nFlight has {current_flight_formatted.stop_overs} "
                      f"stop over, via {current_flight_formatted.via_city}.")

            if int(current_flight_formatted['price']) < int(IATA["lowestPrice"]):
                print("Best price!")
        except IndexError:
            pass


