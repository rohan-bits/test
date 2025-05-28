import asyncio
import websockets
import json


from azure.messaging.webpubsubservice import WebPubSubServiceClient

async def connect(url):
    async with websockets.connect(url) as ws:
        print('Connected')
        while True:
            rec = await ws.recv()
            json.loads(rec)
            print('Received message: ' + rec)
            
            
if __name__ == '__main__':
    service = WebPubSubServiceClient.from_connection_string('Endpoint=https://koili-iot.webpubsub.azure.com;AccessKey=4cUcrZ0LFoOPq0Hsksh85qBjBFXrrDYbNIKKj9zzEBvL3YE3hOKBJQQJ99BBACGhslBXJ3w3AAAAAWPSMlmy;Version=1.0;', hub='Hubs')
    token = service.get_client_access_token()
    #print(token)
    
    try:
        asyncio.get_event_loop().run_until_complete(connect(token['url']))
    except KeyboardInterrupt:
        pass
    