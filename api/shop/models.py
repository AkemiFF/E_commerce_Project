from django.db import models
from django.urls import reverse
from accounts.models import Shopper


class Order(models.Model):
    order_date = models.DateField(null=True, blank=True)
    status = models.SmallIntegerField(null=True, blank=True)
    payment_details = models.CharField(max_length=45, null=True, blank=True)
    client = models.ForeignKey(Shopper, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.status


class Cart(models.Model):
    # quantity = models.CharField(max_length=45)
    total_price = models.CharField(max_length=45, null=True, blank=True)
    client = models.ForeignKey(Shopper, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)


class OrderDetail(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.CharField(max_length=45, null=True, blank=True)
    unit_price = models.CharField(max_length=45, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product


class Invoice(models.Model):

    total_amount = models.CharField(max_length=45, null=True, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Product(models.Model):

    product_name = models.CharField(max_length=45)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="Products", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produit"

    def __str__(self) -> str:
        return self.product_name


class InvoiceDetail(models.Model):
    unit_price = models.IntegerField()
    quantity = models.IntegerField()
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)


class ProductHasCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
