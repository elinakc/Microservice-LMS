# consumers.py in borrowing_books_service

import pika
import json

RABBITMQ_URL = "amqps://vposmrrw:C3kfYDVd059rPsugtOUCsn89uvCqjMkS@armadillo.rmq.cloudamqp.com/vposmrrw"  

params = pika.URLParameters(RABBITMQ_URL)

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange='borrow_exchange', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='borrow_exchange', queue=queue_name)

def borrow_consumer(channel, method, properties, body):
    message = json.loads(body)
    print("Received message:", message)
    # Process the message as needed

channel.basic_consume(queue=queue_name, on_message_callback=borrow_consumer, auto_ack=True)

print("Started Consuming...")
channel.start_consuming()
