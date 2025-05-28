import pika, sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue = 'task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
                      exchange='',
                      routing_key = 'task_queue',
                      body = message,
                      properties = pika.BasicProperties(
                          #Queue won't be lost even after RabbitMQ restarts
                          delivery_mode= pika.DeliveryMode.Persistent
                      ))

print(f" [X] Sent {message}")
connection.close()