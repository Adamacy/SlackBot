# SlackBot

Only thing you have to do is to create file url.txt and paste there last part of webhook URL

To do it add incoming-webhook to your Slack channel. You can use this link: https://test-dg14563.slack.com/apps/A0F7XDUAZ-incoming-webhooks?tab=more_info

## Message content

In this place: 
```python
message = ("書くレポートがあります")
title = (f"New Incoming Message :zap:")
```

You can choose message content and message title.

```python
"icon_emoji": ":satellite:",
```
In this line you can choose Bot avatar (icon)

#Packages

You have to download one package. You can do it with this command.
```
pip install schedule
```

To run program on docker you have to use this two commands in terminal.

```
docker build -t slackbot .
```
```
docker run slackbot
```
You have to be in SlackBot directory.
