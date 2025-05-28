import pika, sys, os

def main():
    # Connecting to rabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue='hello')
    
    # Prints message contents in the screen
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
    
    # tells rabbitmq that this particular function receives message    
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack= True)
    
    print( ' [*] Waiting for message.')
    channel.start_consuming()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)