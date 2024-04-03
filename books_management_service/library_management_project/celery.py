# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_management_project.settings')

# Create a Celery app
app = Celery('books_management_service')

# Load configuration from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover and auto-import task modules
app.autodiscover_tasks()
