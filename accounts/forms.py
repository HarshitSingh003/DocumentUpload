from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginForm(AuthenticationForm):
    # username = forms.CharField(label="Username", max_length=30)
    # password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput)
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].label = "Username"
    #     self.fields['password'].label = "Password"
    #     self.fields['password'].widget = forms.PasswordInput()
    pass