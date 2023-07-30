from django.shortcuts import render
from django.views import View




class CartPage(View):
    def get(self, request):
        return render(request, 'cart.html')


