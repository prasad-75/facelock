# consumers.py
# consumers.py

import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class VideoStreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # self.send (text_data=json.dumps({'type':'connection_established',
        #                                   'message':'You are now connected'
        #                                   }))

    async def disconnect(self, close_code):
        pass
        # await self.channel_layer.group_discard(self.channel_name)
        # print("disconnected")

    async def receive(self, text_data):
        video_data = json.loads(text_data)
        message=video_data['message']
        print('Message:',message)
        


 











        # print(video_data)
        # cap = cv2.VideoCapture(video_data)
        # ret, frame = cap.read()

        # while True:

        #     cv2.imshow("Video", frame)
        #     cv2.waitKey(1)

        #     if cv2.waitKey(25) & 0xFF == ord('q'):
        #         break
        # Process the received video_data (e.g., save to a file, analyze frames, etc.)
        await asyncio.sleep(0)  # Simulate some processing time
        # Send a response back if needed
        await self.send(text_data=json.dumps({'status': 'Processed successfully'}))

