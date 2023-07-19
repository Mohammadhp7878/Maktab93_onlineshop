from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    phone_number = forms.CharField()

    class Meta:
        model = User
        fields = ['phone_number']