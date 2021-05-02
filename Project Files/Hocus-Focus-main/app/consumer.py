import asyncio
from app import prototype
from app.models import *
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class StudentConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("DistracNot", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("DistracNot", self.channel_name)

    async def send_options(self, event):
        q=0
        while True:
            try:
                trigger=Trigger.objects.get(name=event["name"])
                q+=1
                options,token=prototype.speech_to_question(event["lang"])
                await self.send_json({"type":"start","qno":str(q),"options":options,"token":token})
                await asyncio.sleep(7)
            except:
                await self.send_json({"type":"stop"})
                break
