import requests
import config

ENDPOINT = 'https://api.sheety.co'
fmtd_endpoint = f'{ENDPOINT}/{config.SHEET_USERNAME}/{config.SHEET_PROJECT}/{config.SHEET_NAME}'
headers = {
    'Authorization': config.SHEET_TOKEN
}


class DataManager:
    def __init__(self):
        self.sheet_data = {}

    def get_destination_data(self):
        get_response = requests.get(url=fmtd_endpoint, headers=headers)
        get_response.raise_for_status()
        response_json = get_response.json()
        self.sheet_data = response_json['prices']
        return self.sheet_data

    def update_destination_codes(self):
        for city in self.sheet_data:
            data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            put_response = requests.put(
                url=f"{fmtd_endpoint}/{city['id']}",
                headers=headers,
                json=data)
            print(put_response.text)
