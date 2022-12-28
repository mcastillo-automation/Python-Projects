from flight_search import FlightSearch
from data_manager import DataManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

if sheet_data[0]['iataCode'] == '':
    city_names = [row['city'] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_code(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data

destinations = {
    data['iataCode']: {
        'id': data['id'],
        'city': data['city'],
        'price': data['lowestPrice'],
    } for data in sheet_data
}

for destination_code in destinations:
    flight = flight_search.check_flights(
        origin_city_code='LAX',
        destination_city_code=destination_code
    )
    if flight is None:
        continue

    if flight.price < destinations[destination_code]["price"]:
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over via {flight.via_city}"
        print(message)
