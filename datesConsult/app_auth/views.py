import json

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import render

from datesConsult.app_auth.models import Contact
from datesConsult.forms.contact_form import ContactForm
from datesConsult.tasks import send_email_task


# Create your views here.
def homepage(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

def contacts(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            c_list = list(Contact.objects.values())
            return JsonResponse({'context': c_list})
        elif request.method == 'POST':
            data = json.load(request)
            c_entry = data.get('data')

            Contact.objects.create(name=c_entry['name'], email=c_entry['email'], message=c_entry["message"])
            return JsonResponse({'status': 'Contact created'}, status=201)

        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return render(request, 'contact_list.html')

def contacts_list(request):
    return render(request, 'contact_list.html')