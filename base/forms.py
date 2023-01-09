from .models import *
from django.forms import  models
from django import forms
from django.forms import ModelForm
from django.http import request
from django.contrib.auth.forms import UserCreationForm


class IlanForm(ModelForm):
    class Meta:
        model = Ilan
        fields = '__all__'
        exclude = ['host','yorumcular']

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email','password1','password2','bio','avatar','phone_no']

class updateListingForm(ModelForm):
    class Meta:
        model = Ilan
        fields='__all__'
        exclude = ['host','yorumcular']