from django.urls import path

from datesConsult.app_auth.views import *

urlpatterns = [
    path('', homepage, name='homepages'),
]