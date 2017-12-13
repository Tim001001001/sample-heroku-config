from time import sleep
API_KEY = "500594999:AAH5Io-AbkrluJUUAVali2EDSaYGFE1TQok"
import requests
import json

URL = "https://api.telegram.org/bot" + API_KEY + "/getUpdates"
print("URL:", URL, "\n")

response = requests.get(URL) # make GET request
updates = response.json() # parse python object from response

print('Standard view:', updates, sep='\n')
print()

print('Pretty view:',
      json.dumps(updates, indent=2, sort_keys=True),
      sep='\n')
from time import *

last_update_id = 0

while True:
    response = requests.get(URL)  # make GET request
    updates = response.json()  # parse python object from response
    last_update_id = last_update_id + 1
    for msg in updates['result']:
        print(msg['message']['text'])

        # requests.get('https://api.telegram.org/bot500594999:AAH5Io-AbkrluJUUAVali2EDSaYGFE1TQok/sendMessage', params=data)

    sleep(10)
