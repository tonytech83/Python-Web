import logging
import time

from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string

"""
# Web application:
- Initiate tasks (Schedule)

# Celery workers:
- Handle tasks
"""


@shared_task
def slow_operation():
    print(f'Slow operation started at {time.time()}')

    time.sleep(2)

    print(f'Slow operation ended at {time.time()}')


@shared_task
def send_example_email(users_count, title):
    logging.info("send_example_email task started")

    # Simulate sending an email
    time.sleep(2)

    context = {
        'title': title,
        'users_count': users_count,
    }

    html_message = render_to_string('web/html_message.html', context)
    logging.info("Sending email...")
    send_mail(
        subject='Welcome to Celery!',
        message='Hello, there!',
        from_email='test@test.com',
        recipient_list=['new@test.com'],
        html_message=html_message,
        fail_silently=False,
    )
    logging.info("Email sent.")
