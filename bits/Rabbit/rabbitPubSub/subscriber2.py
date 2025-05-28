import pika, sys, os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    channel.exchange_declare(exchange='logs', exchange_type='fanout')
    
    result = channel.queue_declare(queue = '', exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange='logs', queue=queue_name)
    
    print(' [*] Waiting for logs')
    
    def callback(ch, method, properties, body):
        print(f" [X] {body}")
    
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True) 
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