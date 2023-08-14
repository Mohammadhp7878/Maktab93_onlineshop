from django.shortcuts import render, redirect
from rest_framework.views import APIView
import random
from utilize import send_otp
from .serializers import  PhoneSerializer, CodeSerializer
import redis
from rest_framework.response import Response
from hashlib import sha256

redis_client = redis.StrictRedis()

class LoginAPI(APIView):
    def post(self, request):
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            code = random.randint(100000, 999999)
            hashed_code = sha256(code.encode()).hexdigest()
            hashed_phone = sha256(phone_number.encode()).hexdigest()
            # send_otp(phone_number, code)
            redis_client.set(phone_number, hashed_code)
            response = Response({"message": "OTP sent successfully"})
            response.set_cookie('phone_number', hashed_phone, 180)
            print(code)
            return response
        else:
            return Response(serializer.errors, status=400)



class VerifyAPI(APIView):
    def post(self, request):
        serializer = CodeSerializer
        if serializer.is_valid():
            user_code = serializer.validated_data['code']
            user_hashed_code = sha256(user_code.encode()).hexdigest()
            phone = request.COOKIES.get('phone_number')
            


# class Register(View):
#     reg_template = "login.html"
#     reg_form = RegisterForm

#     def get(self, request):
#         form = self.reg_form()
#         return render(request, self.reg_template, {"form": form})

#     def post(self, request):
#         form = self.reg_form(request.POST)

#         if form.is_valid():
#             phone_number = form.cleaned_data["phone_number"]
#             code = random.randint(10000, 99999)
#             send_otp(phone_number, code)
#             request.session["register_form"] = {"phone_number": phone_number}
#             return redirect("verify_code")


# class Verify(View):
#     template = "verify.html"
#     code_form = OtpCodeForm

#     def get(self, request):
#         form = self.code_form()
#         return render(request, self.template, {"form": form})

#     def post(self, request):
#         user_phone = request.session["register_form"]["phone_number"]
#         form = self.form(request.POST)

#         if form.is_valid():
#             print("fine")
