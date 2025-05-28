import asyncio
import sys
import websockets
import ssl
from azure.messaging.webpubsubservice import WebPubSubServiceClient

async def connect(url):
    async with websockets.connect( uri=url) as ws:
        print('connected')
        while True:
            print('Received message: ' + await ws.recv())
            
if __name__ == '__main__':
        
    connection_string = 'Endpoint=https://koili-iot.webpubsub.azure.com;AccessKey=7MVqhSVqEbf9pkYXcJUqIFOUz8pkcrj8BW9mXAmvISy4Wmcf2UyCJQQJ99BBACGhslBXJ3w3AAAAAWPSyXsM;Version=1.0;'
    hub_name = 'Hubs'
    
    service = WebPubSubServiceClient.from_connection_string(connection_string, hub = hub_name)
    token = service.get_client_access_token()
    print(token)
    try:
        asyncio.get_event_loop().run_until_complete(connect(token['url']))
    except KeyboardInterrupt:
        pass