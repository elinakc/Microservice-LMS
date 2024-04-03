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



def publish_borrow_book(book_id):
    try:
        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        channel.exchange_declare(exchange='borrow_exchange', exchange_type='fanout')

        message = {
            'type': 'borrow_book',
            'book_id': book_id
        }

        channel.basic_publish(exchange='borrow_exchange', routing_key='', body=json.dumps(message))

        print(f" [x] Sent borrow book request: {message}")

        connection.close()
        return 'sent'
    except Exception as e:
        print(f"Error publishing borrow book message: {str(e)}")
        return 'error'


















# #OLD CODE

# # import pika
# # import json

# # from django.conf import settings

# # # class BookProducer:
# # #     def __init__(self, book_id):
# # #         self.book_id = book_id

# # def publish_borrowed_book( book_id):  
# #         try:
            
# #             # connection = pika.BlockingConnection(pika.ConnectionParameters(
# #             #     host=settings.RABBITMQ_HOST,
# #             #     port=settings.RABBITMQ_PORT,
# #             #     credentials=pika.PlainCredentials(
# #             #         settings.RABBITMQ_USERNAME, settings.RABBITMQ_PASSWORD),
# #             #     virtual_host=settings.RABBITMQ_VHOST,
# #             # ))
            
# #             amqp_url = "amqps://vposmrrw:C3kfYDVd059rPsugtOUCsn89uvCqjMkS@armadillo.rmq.cloudamqp.com/vposmrrw"

            
# #             connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
            
# #             channel = connection.channel()
# #             channel.queue_declare(queue='borrow_queue')

# #             message = {
# #                 'book_id': book_id
# #             }
            
            
# #             channel.basic_publish(exchange='borrow_exchange', routing_key='borrowed_books', body=json.dumps(message))

# #             print(f" [x] Sent: {message}")
# #             connection.close()
# #         except Exception as e:
# #             print(f"Error publishing message: {str(e)}")
            

# # # Example usage:
# # # if __name__ == "__main__":
# # #     book_id = 123  # Example book ID
# # #     producer = BookProducer(book_id)
# # #     producer.publish_borrowed_book()
