# borrowing_books_app/tasks.py
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import borrow
from celery import Task

class ProcessReturnTask(Task):
    name = 'borrowing_books_app.process_return'

    def run(self, book_id, user_id):
        # Process book return logic here
        borrowed_book = borrow.objects.get(book_id=book_id, user_id=user_id)
        borrowed_book.return_book()
        return f"Book returned successfully: {borrowed_book.book.title}"

class ProcessOverdueNotificationTask(Task):
    name = 'borrowing_books_app.process_overdue_notification'

    def run(self, book_id, user_id):
        # Process overdue notification logic here
        borrowed_book = borrow.objects.get(book_id=book_id, user_id=user_id)
        borrowed_book.send_overdue_notification()
        return f"Overdue notification sent for book: {borrowed_book.book.title}"