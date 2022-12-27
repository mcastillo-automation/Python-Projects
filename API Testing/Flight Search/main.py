from flight_search import FlightSearch
from data_manager import DataManager

sheet = DataManager()
sheet_data = sheet.get_destination_date()
flight_search = FlightSearch()

if sheet_data[0]['iataCode'] == '':
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    sheet.sheet_data = sheet_data
    sheet.put_destination_data()

for destination in sheet_data:
    flight = flight_search.search(
        origin_city_code='LON',
        destination_city_code=destination['iataCode']
    )