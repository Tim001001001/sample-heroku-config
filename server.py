import datetime
import requests
import json
from time import *
import handler
API_KEY = "500594999:AAH5Io-AbkrluJUUAVali2EDSaYGFE1TQok"
URL = "https://api.telegram.org/bot" + API_KEY + "/getUpdates"
print("URL:", URL, "\n")
weday = datetime.datetime.now()

response = requests.get(URL)  # make GET request
updates = response.json()  # parse python object from response


last_update_id = 0

while True:
    offs = {
        'offset': last_update_id
    }
    response = requests.get(URL, params=offs)  # make GET request
    updates = response.json()  # parse python object from response

    for msg in updates['result']:
        # print(msg['message']['text'])
        last_update_id = msg["update_id"] + 1
        text = msg["message"]["text"]
        ans = handler.handle_message(text)
        chat_id = msg["message"]["chat"]["id"]
        requests.post("https://api.telegram.org/bot" + API_KEY + "/sendMessage", params={"chat_id": chat_id, "text": ans})

    sleep(1)
