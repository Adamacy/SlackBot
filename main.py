import json
import sys
import requests
import time
import datetime

f = open('url.txt', 'r')
data = f.read()

uri = f'https://hooks.slack.com/services/{data}'
message = ("書くレポートがあります")  # Message
title = (f"New Incoming Message :zap:")  # Message Title
slack_data = {
    "username": "NotificationBot",
    "icon_emoji": ":satellite:",
    "attachments": [
        {
                "color": "#ff00ff",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
        }
    ]
}


def main():
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json",
        'Content-Length': byte_length}
    requests.post(uri, data=json.dumps(slack_data), headers=headers)
    print('Message Sent')

while True:
    now = datetime.datetime.now().strftime('%H:%M')
    if now == "16:00":
        main()
    time.sleep(30)
