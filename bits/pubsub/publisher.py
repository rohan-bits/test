from azure.messaging.webpubsubservice import WebPubSubServiceClient
from app import app

if __name__ == '__main__':
    connection_string = 'Endpoint=https://koili-iot.webpubsub.azure.com;AccessKey=4cUcrZ0LFoOPq0Hsksh85qBjBFXrrDYbNIKKj9zzEBvL3YE3hOKBJQQJ99BBACGhslBXJ3w3AAAAAWPSMlmy;Version=1.0;'
    hub_name = 'Hubs'
    message = ({"amount":"amount", 
            "termination_id":"termination_id"})
    
    service = WebPubSubServiceClient.from_connection_string(connection_string, hub=hub_name)
    res = service.send_to_all(message, content_type='application/json')
    
    