from django.forms import Form, ModelForm, CharField, TextInput, BooleanField, IntegerField, EmailField, ModelChoiceField
from django.db import models
from main.models import Category

class UserDataForm(Form):
    first_name = CharField(required=True,label='First Name', widget=TextInput()) 
    last_name = CharField(required=True,label='Last Name', widget=TextInput())
    email = EmailField(required=True,label='Email', widget=TextInput())
#    category = ModelChoiceField(label='Status', queryset=Category.objects.all().order_by('name'), initial=0)
