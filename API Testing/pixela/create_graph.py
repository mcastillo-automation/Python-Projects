"""
Messing around with the Pixela api. Available here: https://pixe.la/
This creates a graph.
"""
import requests
import config


ENDPOINT = 'https://pixe.la/v1/users'
graph_endpoint = f'{ENDPOINT}/{config.USERNAME}/graphs'

headers = {
    'X-USER-TOKEN': config.TOKEN
}
request_body = {
    'id': config.GRAPH_ID,
    'name': 'Coding Practice',
    'unit': 'commit',
    'type': 'int',
    'color': 'shibafu'
}

response = requests.post(url=graph_endpoint, headers=headers, json=request_body)
print(response.text)
