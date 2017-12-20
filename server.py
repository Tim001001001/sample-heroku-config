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
    offs={
        'offset': last_update_id
    }
    response = requests.get(URL,params=offs)  # make GET request
    updates = response.json()  # parse python object from response

    for msg in updates['result']:
        print(msg['message']['text'])
        last_update_id = msg["update_id"] +1
        if (msg['message']['text']=="1"):
            data = {
                'chat_id': 426464786,
                'text': 'wwwww'
                }
            requests.get('https://api.telegram.org/bot500594999:AAH5Io-AbkrluJUUAVali2EDSaYGFE1TQok/sendMessage', params=data)
        elif(msg['message']['text']=="2"):
            data = {
                'chat_id': 426464786,
                'text': " subject Li,teacherName D,roomNumber 201 subject Ch,teacherName EV,roomNumber 409 subject Math,teacherName EBroomNumber 206 "
            }
            requests.get('https://api.telegram.org/bot500594999:AAH5Io-AbkrluJUUAVali2EDSaYGFE1TQok/sendMessage', params=data)
        elif(msg['message']['text']=="3"):
            data = {
                'chat_id': 426464786,
                'text': " subject ,teacherName D,roomNumber 201 subject Ch,teacherName EV,roomNumber 409 subject Math,teacherName EBroomNumber 206 ",
            }
            requests.get('https://api.telegram.org/bot500594999:AAH5Io-AbkrluJUUAVali2EDSaYGFE1TQok/sendMessage', params=data)
        elif(msg['message']['text']=="4"):
            data = {
                'chat_id': 426464786,
                'text': " subject ru,teacherName D,roomNumber 201 subject Ch,teacherName EV,roomNumber 409 subject Math,teacherName EBroomNumber 206 ",
            }
            requests.get('https://api.telegram.org/bot500594999:AAH5Io-AbkrluJUUAVali2EDSaYGFE1TQok/sendMessage', params=data)
        elif(msg['message']['text']=="5"):
            data = {
                'chat_id': 426464786,
                'text': " subject __ teacherName D,roomNumber 201 subject Ch,teacherName EV,roomNumber 409 subject Math,teacherName EBroomNumber 206 ",
            }
            requests.get('https://api.telegram.org/bot500594999:AAH5Io-AbkrluJUUAVali2EDSaYGFE1TQok/sendMessage', params=data)
        elif(msg['message']['text']=="6"):
            data = {
                'chat_id': 426464786,
                'text': " no lessons ",
            }
            requests.get('https://api.telegram.org/bot500594999:AAH5Io-AbkrluJUUAVali2EDSaYGFE1TQok/sendMessage', params=data)
        elif (msg['message']['text'] == "7"):
           data = {
               'chat_id': 426464786,
               'text': "  no lessons ",
            }
           requests.get('https://api.telegram.org/bot500594999:AAH5Io-AbkrluJUUAVali2EDSaYGFE1TQok/sendMessage',
                        params=data)
        else:
            data = {
                'chat_id': 426464786,
                'text': "  Error ",
            }
            requests.get('https://api.telegram.org/bot500594999:AAH5Io-AbkrluJUUAVali2EDSaYGFE1TQok/sendMessage',
                         params=data)
    sleep(1)
