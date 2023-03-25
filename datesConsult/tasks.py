from time import sleep

from celery.utils.log import get_task_logger
from django.core.mail import send_mail
from celery import shared_task

logger = get_task_logger(__name__)


@shared_task()
def send_email_task(subject, message, from_email, recipients):
    """Sends an email to recipients."""
    sleep(20)  # Simulate expensive operation(s) that freeze Django
    for email in recipients:
        send_mail(
            subject,
            message,
            from_email,
            [email],
            fail_silently=False,
        )
        logger.info("Email sent successfully.....")