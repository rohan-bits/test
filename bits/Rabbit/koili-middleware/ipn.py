import pika

QUEUE_NAME = 'ipn_service'

def start_consuming():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)
    
    channel.exchange_declare(exchange='exchange', exchange_type='fanout')

    
    channel.queue_bind(exchange='exchange',queue=QUEUE_NAME)
    
    def callback(ch, method, properites, body):
        print(f'[x] received {body}')
        
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)
    
    print('[*] Waiting for message')
    
    channel.start_consuming()
    
if __name__ == '__main__':
    start_consuming()