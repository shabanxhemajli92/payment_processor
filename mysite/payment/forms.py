from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'custom-class', 'placeholder':'Your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'custom-class'}))