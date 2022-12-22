"""
Messing around with the Pixela api. Available here: https://pixe.la/
This allows a user to add a dot to their pixela graph.
"""

import datetime
import requests
import config

ENDPOINT = 'https://pixe.la/v1/users'
graph_endpoint = f'{ENDPOINT}/{config.USERNAME}/graphs/{config.GRAPH_ID}'
current_day = datetime.date.today().strftime('%Y%m%d')

headers = {
    'X-USER-TOKEN': config.TOKEN
}
request_body = {
    'date': current_day,
    'quantity': '1'
}

response = requests.post(url=graph_endpoint, headers=headers, json=request_body)
print(response.text)
