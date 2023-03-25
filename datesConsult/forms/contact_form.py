from django import forms

from datesConsult.app_auth.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"