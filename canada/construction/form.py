from .models import ContactForm as ContactFormModel
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model =  ContactFormModel
        fields = ['name','number', 'comment']

