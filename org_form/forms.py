# Michael McGuirk - D13123389
# DT228/4 - Final Year Project

from django.db import models
from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from .models import Organisation
from django.contrib.auth.models import User

form_control_attr = {'class': 'form-control'}

class NewOrgForm(ModelForm):
    name = forms.CharField(
        widget = forms.TextInput(attrs=form_control_attr))
    email = forms.CharField(
        widget = forms.TextInput(attrs=form_control_attr))
    address_1 = forms.CharField(
        widget = forms.TextInput(attrs=form_control_attr))
    address_2 = forms.CharField(
        widget = forms.TextInput(attrs=form_control_attr))
    address_3 = forms.CharField(
        widget = forms.TextInput(attrs=form_control_attr))
    zip_code = forms.CharField(
        widget = forms.TextInput(attrs=form_control_attr))
    state = forms.CharField(
        widget = forms.TextInput(attrs=form_control_attr))
    country = forms.CharField(
        widget = forms.TextInput(attrs=form_control_attr))
    contact_no = forms.CharField(
        widget = forms.TextInput(attrs=form_control_attr))

    class Meta:
        model = Organisation
        fields = ['name', 'email', 'address_1', 'address_2', 
        'address_3', 'zip_code', 'state', 'country', 
        'contact_no']



# class UserForm(ModelForm):
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}))

#     email = forms.CharField(
#         widget=forms.EmailInput(attrs={'class': 'form-control'}))

#     username = forms.CharField(
#         widget = forms.TextInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')

# class UserSettingsForm(ModelForm):

#     def_temp_low = forms.FloatField(
#         widget = forms.NumberInput(attrs={'class': 'form-control'}))

#     def_temp_high = forms.FloatField(
#         widget = forms.NumberInput(attrs={'class': 'form-control'}))    

#     class Meta:
#         model = UserBatchSettings
#         fields = ['def_temp_low', 'def_temp_high', 'def_temp_format']