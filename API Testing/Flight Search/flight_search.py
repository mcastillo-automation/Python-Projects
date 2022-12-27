import requests
import datetime
from flight_data import FlightData
import config

ENDPOINT = 'https://api.tequila.kiwi.com'
header = {
    'apikey': config.FLIGHT_SEARCH_API_KEY
}


class FlightSearch:

    def search(self, origin_city_code, destination_city_code):
        search_data = {
            'fly_from': origin_city_code,
            'fly_to': destination_city_code,
            'date_from': (datetime.datetime.now() + datetime.timedelta(1)).strftime('%d/%m/%Y'),
            'date_to': (datetime.datetime.now() + datetime.timedelta(6 * 30)).strftime('%d/%m/%Y'),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'one_for_city': 1,
            'max_stopovers': 0,
            'curr': 'GBP'
        }
        search_response = requests.get(url=f'{ENDPOINT}/v2/search', headers=header, params=search_data)
        search_response.raise_for_status()
        try:
            search_response_json = search_response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None

        flight_data = FlightData(
            price=search_response_json['price'],
            origin_city=search_response_json["route"][0]["cityFrom"],
            origin_airport=search_response_json["route"][0]["flyFrom"],
            destination_city=search_response_json["route"][0]["cityTo"],
            destination_airport=search_response_json["route"][0]["flyTo"],
            out_date=search_response_json["route"][0]["local_departure"].split("T")[0],
            return_date=search_response_json["route"][1]["local_departure"].split("T")[0]
        )
        print(f'{flight_data.destination_city}: £{flight_data.price}')
        return flight_data

    def get_destination_code(self, city_name):
        dest_data = {
            'term': city_name
        }
        dest_code_response = requests.get(url=f'{ENDPOINT}/locations/query', headers=header, params=dest_data)
        dest_code_response.raise_for_status()
        dest_code_response_json = dest_code_response.json()
        dest_code = dest_code_response_json['locations'][0]['code']
        return dest_code
