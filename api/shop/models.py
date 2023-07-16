from django.db import models
from accounts.models import Shopper


class Cart(models.Model):
    quantity = models.CharField(max_length=45)
    total_price = models.CharField(max_length=45, null=True, blank=True)
    client = models.ForeignKey(Shopper, on_delete=models.CASCADE)


class Order(models.Model):
    order_date = models.DateField(null=True, blank=True)
    status = models.SmallIntegerField(null=True, blank=True)
    payment_details = models.CharField(max_length=45, null=True, blank=True)
    client = models.ForeignKey(Shopper, on_delete=models.CASCADE)


class OrderDetail(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.CharField(max_length=45, null=True, blank=True)
    unit_price = models.CharField(max_length=45, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Invoice(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    total_amount = models.CharField(max_length=45, null=True, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=45)
    description = models.CharField(max_length=145, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)


class InvoiceDetail(models.Model):
    unit_price = models.IntegerField()
    quantity = models.IntegerField()
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)


class ProductHasCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
