import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-z$1br(*hv8ta510wfqi4cqw$9)806e*6$#*sa$q$(u102j#fx@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party libraries:
    'channels',

    # Custom:
    'datesConsult.app_auth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'datesConsult.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ASGI_APPLICATION = 'dataConsult.asgi.application'
WSGI_APPLICATION = 'datesConsult.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dates_consult2',
        'USER': 'postgres',
        'PASSWORD': '1123QwER',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
if DEBUG:
    AUTH_PASSWORD_VALIDATORS = []
else:
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# User model:
AUTH_USER_MODEL = 'app_auth.CustomUser'

# Mailtrap settings
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '05723b4b5b62ff'
EMAIL_HOST_PASSWORD = 'ea571a165f1452'
EMAIL_PORT = '2525'


# Celery settings
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"
CELERY_TIMEZONE = "Europe/Sofia"

# scheduler configuration
# Always start the celery worker before starting beats
# run:  celery -A datesConsult beat -l info
from celery.schedules import crontab

# scheduler configuration
# https://docs.celeryq.dev/en/latest/userguide/periodic-tasks.html
CELERY_BEAT_SCHEDULE = {
    'Task_one_schedule' : {  # whatever the name you want
        'task': 'datesConsult.tasks.send_email_task', # {app_name}.tasks.{task_name}
        'schedule': crontab(hour=7, minute=30, day_of_week=1), # Executes every Monday morning at 7:30 a.m.
        'args': ('New offer', 'Message one',  'admin@company.com', ['test@abv.bg']), # arguments for the task
        'options': {
            'expires': 30.0, # if it's not able to run this task within 15 seconds, to just cancel it
        },
    },
}