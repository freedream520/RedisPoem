#coding=utf-8
from django import forms
from django.forms import ModelForm
import random
from django.conf import settings


class LoginForm(forms.Form):
    us = forms.CharField(label=u'用户名',max_length=100,widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': u'用户名', 'required': '', 'autofocus': ''}
        ),
    )
    pwd = forms.CharField(label=u'密码',widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': u'密码', 'required': ''}
        )
    )







