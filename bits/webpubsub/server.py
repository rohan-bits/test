from azure.messaging.webpubsubservice import WebPubSubServiceClient
from azure.core.credentials import AzureKeyCredential

# Initialize WebPubSub client
client = WebPubSubServiceClient.from_connection_string('Endpoint=https://koili-iot.webpubsub.azure.com;AccessKey=7MVqhSVqEbf9pkYXcJUqIFOUz8pkcrj8BW9mXAmvISy4Wmcf2UyCJQQJ99BBACGhslBXJ3w3AAAAAWPSyXsM;Version=1.0;',
    hub="Hubs"
)

# Publish a message to all connected clients
client.send_to_all(message="Hello, subscribers!", content_type="text/plain")
