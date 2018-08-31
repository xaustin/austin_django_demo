# -*- coding: utf-8 -*-
from django import forms


# 登录
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
