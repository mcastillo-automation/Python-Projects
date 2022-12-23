"""
Messing around with Nutritionix and Sheety.
Queries user via console for exercise and updates a Google sheet.
"""

import requests
import datetime
import config

N_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-id': config.APP_ID,
    'x-app-key': config.API_KEY
}

data = {
    'query': input('What exercises did you do? '),
    'gender': config.GENDER,
    'weight_kg': config.WEIGHT,
    'height_cm': config.HEIGHT,
    'age': config.AGE
}

n_response = requests.post(url=N_ENDPOINT, headers=headers, json=data).json()

G_ENDPOINT = 'https://api.sheety.co'
fmtd_g_endpoint = f'{G_ENDPOINT}/{config.USERNAME}/{config.PROJECT_NAME}/{config.SHEET_NAME}'

g_header = {
    'Authorization': config.TOKEN
}

exer_data = {
    'workout': {
        'date': datetime.date.today().strftime('%d/%m/%Y'),
        'time': datetime.datetime.now().strftime('%X'),
        'exercise': n_response['exercises'][0]['name'].title(),
        'duration': n_response['exercises'][0]['duration_min'],
        'calories': n_response['exercises'][0]['nf_calories']
    }
}

g_response = requests.post(url=fmtd_g_endpoint, headers=g_header, json=exer_data)
print(g_response.text)
