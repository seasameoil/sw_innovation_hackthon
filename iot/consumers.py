import json
from random import randint
from datetime import datetime
# from time import sleep
from asyncio import sleep

from channels.generic.websocket import AsyncWebsocketConsumer

from iot.iot import count, fire, crime


class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:

            await self.send(json.dumps({'count':count, 'fire':fire, 'crime':crime}))
            await sleep(2)