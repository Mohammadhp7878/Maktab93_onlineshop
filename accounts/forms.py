from django import forms
from .models import User, OtpCode

class RegisterForm(forms.ModelForm):
    phone_number = forms.CharField()

    class Meta:
        model = User
        fields = ['phone_number']

class OtpCodeForm(forms.ModelForm):
    code = forms.CharField()

    class Meta:
        model = OtpCode
        fields = ['code']