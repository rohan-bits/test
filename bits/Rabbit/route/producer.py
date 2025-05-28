import pika
from pika.exchange_type import ExchangeType

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)

message = 'This message is to be routed'

channel.basic_publish(exchange='routing',
                      routing_key='analyticsonly',
                      body = message)

print(f"sent message: {message}")

connection.close()