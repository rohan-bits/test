import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

message = ' '.join(sys.argv[1:]) or "Hello World234!"

channel.queue_declare(queue = 'hello')
channel.queue_declare(queue = 'hello1')

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body = message)

print("[X] Sent the message")

channel.close()

#purge message
# rabbitmqadmin purge queue_name = 'hello'

#removed unacked message
# list down unacked q
# rabbitmqctl list_queues name message; messages_unacknowledged

# view conection
# rabbitmqctl list_channels connection; messages_unacknowledged

