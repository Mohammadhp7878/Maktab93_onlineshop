from django.shortcuts import render
from django.views import View
from .forms import RegisterForm

class Register(View):
    reg_template = 'register.html'
    form = RegisterForm

    def get(self, request):
        return render(request, self.reg_template, self.form)

