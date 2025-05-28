from azure.messaging.webpubsubservice import WebPubSubServiceClient

if __name__ == "__main__":
    connection_string = 'Endpoint=https://koili-iot.webpubsub.azure.com;AccessKey=7MVqhSVqEbf9pkYXcJUqIFOUz8pkcrj8BW9mXAmvISy4Wmcf2UyCJQQJ99BBACGhslBXJ3w3AAAAAWPSyXsM;Version=1.0;'
    hub_name = 'Hubs'
    message = "Hello Warald!!"
    attributes = {
        "prefix": "IPNT",
        "serial_number": "6557989"
    }
    
service = WebPubSubServiceClient.from_connection_string(connection_string, hub = hub_name)
res = service.send_to_all(message, content_type='text/plain')
print(message, attributes)