# myapp/forms.py
from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, label='姓名')
    email = forms.EmailField(label='电子邮件')
    password = forms.CharField(widget=forms.PasswordInput, label='密码')