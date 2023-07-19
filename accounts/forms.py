from django import forms


class RegisterForm(forms.ModelForm):
    phone_number = forms.EmailField()