import json
import sys
import requests
import schedule, time

f = open('SlackBot/url.txt', 'r')
data = f.read()

uri = f'https://hooks.slack.com/services/{data}'
message = ("書くレポートがあります") #Message
title = (f"New Incoming Message :zap:") #Message Title
slack_data = {
    "username": "NotificationBot",
    "icon_emoji": ":satellite:",
    "attachments": [
        {
                "color": "#9733EE",
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
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    res = requests.post(uri, data=json.dumps(slack_data), headers=headers)

schedule.every().day.at("16:00").do(main) #Time to send message

while True:
    schedule.run_pending()
    time.sleep(60)