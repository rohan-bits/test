import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Creating a queue
channel.queue_declare(queue='hello')

channel.basic_publish(exchange = '',
                      routing_key='hello',
                      body = "Hello Warald!")
print(" [x] Sent 'Hello World!'")

connection.close()

