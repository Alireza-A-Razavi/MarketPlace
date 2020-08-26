from django.contrib import admin
from .models import Order, OrderItem, Address, Coupon, Refund

admin.site.register(Order)
admin.site.register(Coupon)
admin.site.register(Address)
admin.site.register(OrderItem)
admin.site.register(Refund)
