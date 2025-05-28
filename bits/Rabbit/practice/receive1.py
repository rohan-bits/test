import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello1')

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

result = channel.queue_declare(queue='hello1')
#queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue='hello1')

def callback(ch, method, properties, body):
    print(f"[X] Received message: {body}")
    #time.sleep(10)
    print("[X] Done")
    #ch.basic_ack(delivery_tag = method.delivery_tag)
    
channel.basic_consume(
    queue='hello1', on_message_callback=callback, auto_ack=False)

print("[*] Waiting for a message")

#channel.basic_qos(prefetch_count=1)

channel.start_consuming()