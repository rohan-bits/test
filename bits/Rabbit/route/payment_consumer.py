import pika
from pika.exchange_type import ExchangeType

def callback(ch, method, properties, body):
    print(f"received message: {body}")
    
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)

queue = channel.queue_declare(queue=' ', exclusive=True)

channel.exchange_bind(exchange = 'routing', queue = queue.method.queue, routing_key='paymentonly')

channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=callback)

print("[*] Waiting to consume")

channel.start_consuming()
    