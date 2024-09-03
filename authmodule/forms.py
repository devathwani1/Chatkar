from django import forms
from django.core.validators import MinValueValidator

class SignupForm(forms.Form):

    template_name = "signup_snippet.html"
    user_email = forms.EmailField(
        label='Email',
        max_length=255,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        label='Firstname',
        max_length=55,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    middle_name = forms.CharField(
        label='Middlename',
        max_length=55,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        label='Lastname',
        max_length=55,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    user_age = forms.IntegerField(
        required=True,
        validators= [MinValueValidator(18)],
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class LoginForm(forms.Form):
    template_name = "signup_snippet.html"
    user_email = forms.EmailField(
        label='Email',
        max_length=255,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
