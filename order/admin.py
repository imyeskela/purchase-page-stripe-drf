from django.contrib import admin

from order.models import Item, Order

admin.site.register(Item)
admin.site.register(Order)
