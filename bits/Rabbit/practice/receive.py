import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

result = channel.queue_declare(queue='hello')
#queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue='hello')

def callback(ch, method, properties, body):
    print(f"[X] Received message: {body}")
    #time.sleep(5)
    print("[X] Done")
    #ch.basic_ack(delivery_tag = method.delivery_tag)
    
channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=False)

#channel.bapic_qos(prefetch_count=1)

print("[*] Waiting for a message")

channel.start_consuming()