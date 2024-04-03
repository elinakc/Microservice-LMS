from django.dispatch import Signal

#define signals
book_returned = Signal()
book_overdue = Signal()

from django.core.mail import send_mail
from django.dispatch import receiver
from .models import Borrow
# from .signals import book_overdue


# Define receiver function for book_overdue signal
@receiver(book_overdue)
def send_overdue_notification(sender, Borrow, **kwargs):
    # subject = "Book Overdue Notification"
    # message = f"Dear {borrow.user.username}, your borrowed book is overdue. Please pay the fine to avoid further penalties."
    # sender_email = "your_email@example.com"  # Update with your email
    # recipient_email = borrow.user.email

    # send_mail(subject, message, sender_email, [recipient_email])
    print("overdue")
    
    
# Define receiver function for book_returned signal
@receiver(book_returned)
def send_return_notification(sender, Borrow, **kwargs):
    # subject = "Book Return Notification"
    # message = f"Dear {borrow.user.username}, your borrowed book has been returned."
    # sender_email = "your_email@example.com"  # Update with your email
    # recipient_email = borrow.user.email

    # send_mail(subject, message, sender_email, [recipient_email])
    print("return ")