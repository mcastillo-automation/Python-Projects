import requests
import datetime
from pprint import pprint
from flight_data import FlightData
import config

TEQUILA_ENDPOINT = 'https://api.tequila.kiwi.com'
header = {
    'apikey': config.FLIGHT_SEARCH_API_KEY
}


class FlightSearch:

    def __init__(self):
        self.city_codes = []

    def get_destination_code(self, city_names):
        print("get destination codes triggered")
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        for city in city_names:
            query = {"term": city, "location_types": "city"}
            response = requests.get(url=location_endpoint, headers=header, params=query)
            results = response.json()["locations"]
            code = results[0]["code"]
            self.city_codes.append(code)

        return self.city_codes

    def check_flights(self, origin_city_code, destination_city_code):
        search_data = {
            'fly_from': origin_city_code,
            'fly_to': destination_city_code,
            'date_from': (datetime.datetime.now() + datetime.timedelta(1)).strftime('%d/%m/%Y'),
            'date_to': (datetime.datetime.now() + datetime.timedelta(6 * 30)).strftime('%d/%m/%Y'),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 30,
            'flight_type': 'round',
            'one_for_city': 1,
            'max_stopovers': 0,
            'curr': 'USD'
        }

        response = requests.get(url=f'{TEQUILA_ENDPOINT}/v2/search', headers=header, params=search_data)

        try:
            search_response_json = response.json()['data'][0]

        except IndexError:
            search_data['max_stopovers'] = 1
            response = requests.get(url=f'{TEQUILA_ENDPOINT}/v2/search', headers=header, params=search_data)

            try:
                search_response_json = response.json()['data'][0]
                pprint(search_response_json)

            except IndexError:
                print(f"No flights found for {destination_city_code}")
                return None

            else:
                flight_data = FlightData(
                    price=search_response_json['price'],
                    origin_city=search_response_json["route"][0]["cityFrom"],
                    origin_airport=search_response_json["route"][0]["flyFrom"],
                    destination_city=search_response_json["route"][0]["cityTo"],
                    destination_airport=search_response_json["route"][0]["flyTo"],
                    out_date=search_response_json["route"][0]["local_departure"].split("T")[0],
                    return_date=search_response_json["route"][1]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=search_response_json["route"][0]["cityTo"]
                )
                print(f'{flight_data.destination_city}: ${flight_data.price}')
                return flight_data

        else:
            flight_data = FlightData(
                price=search_response_json['price'],
                origin_city=search_response_json["route"][0]["cityFrom"],
                origin_airport=search_response_json["route"][0]["flyFrom"],
                destination_city=search_response_json["route"][0]["cityTo"],
                destination_airport=search_response_json["route"][0]["flyTo"],
                out_date=search_response_json["route"][0]["local_departure"].split("T")[0],
                return_date=search_response_json["route"][1]["local_departure"].split("T")[0]
            )
            print(f'{flight_data.destination_city}: ${flight_data.price}')
            return flight_data
