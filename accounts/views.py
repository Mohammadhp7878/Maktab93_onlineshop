from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, OtpCodeForm
import random
from utilize import send_otp
class Register(View):
    reg_template = 'register.html'
    reg_form = RegisterForm

    def get(self, request):
        form = self.reg_form()
        return render(request, self.reg_template, {'form':form})
    
    def post(self, request):
        form = self.reg_form(request.POST)

        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            code = random.randint(10000, 99999)
            send_otp(phone_number, code)
            request.session['register_form'] = {'phone_number':phone_number}
            return redirect('verify_code')

class Verify(View):
    template = 'verify.html'
    code_form = OtpCodeForm

    def get(self, request):
        form = self.code_form()
        return render(request, self.template, {'form':form})
    
    def post(self, request):
        user_phone = request.session['register_form']['phone_number']
        form = self.form(request.POST)

        if form.is_valid():
            print('fine')