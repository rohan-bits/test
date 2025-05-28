import pika, sys, os

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange = 'logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info:Hello World!"
channel.basic_publish(exchange= 'logs',
                      routing_key = 'hello',
                      body = message)

# Creating a queue and letting server rename it
result = channel.queue_declare(queue= '', exclusive=True)

channel.queue_bind(exchange='logs',
                   queue = result.method.queue)