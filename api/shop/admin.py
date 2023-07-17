from django.contrib import admin

from shop.models import OrderDetail, Product, Order, Cart, Invoice, InvoiceDetail

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Cart)
admin.site.register(Invoice)
admin.site.register(InvoiceDetail)
