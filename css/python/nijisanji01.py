#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from apiclient.discovery import build

API_KEY = 'AIzaSyBoaa14uzdor3FZ6KjaZOUsUrgPxu6EG6o'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
CHANNEL_ID = 'UCD-miitqNY3nyukJ4Fnf4_A'

youtube = build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerKey=API_KEY
)

response = youtube.search().list(
    part = "id",
    channelId = CHANNEL_ID,
    maxResults = 15,
    order = "date" #日付順にソート
    ).execute()


with open("response.json", mode="w", encoding="utf-8") as f:
    json.dump(response, f, ensure_ascii=False, indent=2)