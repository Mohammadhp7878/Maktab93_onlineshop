from django.contrib import admin
from . import models


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['status', 'deliver_time', 'total_price']
    list_filter = ['status']