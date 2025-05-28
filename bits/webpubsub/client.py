from azure.messaging.webpubsubclient import WebPubSubClient
from azure.messaging.webpubsubclient.models import CallbackType
# Define the service URL and hub name
client = WebPubSubClient('wss://koili-iot.webpubsub.azure.com/client/hubs/Hub?access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ3c3M6Ly9rb2lsaS1pb3Qud2VicHVic3ViLmF6dXJlLmNvbS9jbGllbnQvaHVicy9IdWIiLCJpYXQiOjE3NDAxMTk1ODMsImV4cCI6MTc0MDEyMzE4M30.Wyr02fLpSLkVE4FTV-2YeqTqAshO_VRp_c-ff5RmNvU')

with client:
    ...

group_name = "group1"
client.subscribe(CallbackType.GROUP_MESSAGE, lambda e: print(f"Message: {e.data}"))

client.join_group(group_name)

client.send_to_group(group_name, "hello warald!!", WebPubSubDataType.TEXT)