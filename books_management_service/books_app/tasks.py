from celery import Celery
from django.core.mail import send_mail
from django.conf import settings

app = Celery('library_management_project')  # Replace 'books_app' with your Django app name

@app.task
def send_borrow_notification(email, book_title, return_date):
    subject = 'Book Borrow Notification'
    message = f'Hello,\n\nYou have borrowed the book "{book_title}". Please return it by {return_date}.'
    sender_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, sender_email, recipient_list)
