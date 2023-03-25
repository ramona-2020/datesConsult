from django.urls import path

from datesConsult.app_auth.views import *

urlpatterns = [
    path('', homepage, name='homepages'),
    path('list/', contacts_list, name='contacts_list'),
    path('contact/', contact, name='contact'),
    path('contacts/', contacts, name='contacts'),
]