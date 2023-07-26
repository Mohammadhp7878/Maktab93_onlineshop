from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


def home(request):
    return render(request, 'home.html') 

class Home(APIView):
    def get(self, request):
        content = {"hello": "world", "title": "home"}
        return Response(data=content)
