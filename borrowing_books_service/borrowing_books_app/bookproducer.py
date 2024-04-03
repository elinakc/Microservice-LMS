# producer.py in books_management_service

import pika
import json

RABBITMQ_URL = "amqps://vposmrrw:C3kfYDVd059rPsugtOUCsn89uvCqjMkS@armadillo.rmq.cloudamqp.com/vposmrrw" 

params = pika.URLParameters(RABBITMQ_URL)

def publish_availability_check(book_id, borrower_id):
    try:
        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        channel.exchange_declare(exchange='borrow_exchange', exchange_type='fanout')

        message = {
            'book_id': book_id,
            'borrower_id': borrower_id
        }

        channel.basic_publish(exchange='borrow_exchange', routing_key='', body=json.dumps(message))

        print(f" [x] Sent availability check request: {message}")

        connection.close()
        return 'sent'
    except Exception as e:
        print(f"Error publishing availability check message: {str(e)}")
        return 'error'


