# SlackBot

Only thing you have to do is to create file url.txt and paste there last part of webhook URL

To do it add incoming-webhook to your Slack channel. You can use this link: https://test-dg14563.slack.com/services/B037EAX9US1?settings=1

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
