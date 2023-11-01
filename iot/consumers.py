import json
from random import randint
from datetime import datetime
# from time import sleep
from asyncio import sleep

from channels.generic.websocket import AsyncWebsocketConsumer

import iot.iot


class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            congestion = 0
            congestion2 = 0


            await self.send(json.dumps({'value1': total, 'cong1': congestion, 'hour': hour,
                                        'value2': total2, 'cong2': congestion2, 'add1': add1, 'add2': add2, 'dir1':dir1, 'dir2':dir2}))
            await sleep(2)
