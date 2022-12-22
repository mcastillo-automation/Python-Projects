"""
Simple concept. Pixela offers the ability to update the quantity set in a previous POST request via
PUT on your Pixela graph provided you have the date. If pixel doesn't exist, it creates it.
"""

import datetime
import requests
import config


ENDPOINT = 'https://pixe.la/v1/users'
current_day = datetime.date.today().strftime('%Y%m%d')
pixel_endpoint = f'{ENDPOINT}/{config.USERNAME}/graphs/{config.GRAPH_ID}/{current_day}'


headers = {
    'X-USER-TOKEN': config.TOKEN
}
request_body = {
    'quantity': '5'
}

response = requests.put(url=graph_endpoint, headers=headers, json=request_body)
print(response.text)
