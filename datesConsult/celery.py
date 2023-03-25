import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datesConsult.settings')

# Create default Celery app
app = Celery("datesConsult")

# namespace='CELERY' means all celery-related configuration keys
# should be uppercased and have a `CELERY_` prefix in Django settings.
# https://docs.celeryproject.org/en/stable/userguide/configuration.htmls
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()