import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

message = ' '.join(sys.argv[1:]) or "The job has been completed!!!"

channel.queue_declare(queue='ipn_service')
channel.queue_declare(queue='sms_service')
channel.queue_declare(queue='email_service')

channel.queue_bind(exchange='exchange', queue='ipn_service')
channel.queue_bind(exchange='exchange', queue='sms_service')
channel.queue_bind(exchange='exchange', queue='email_service')


channel.exchange_declare(exchange='exchange', exchange_type='fanout')


channel.basic_publish(exchange='exchange',
                      routing_key='',
                      body = message)

print("[X] Sent the message")

channel.close()
