import os
from string import ascii_lowercase
from django.db import models
from django.urls import reverse
from accounts.models import Shopper
from shutil import move
from django.core.files import File as FileWrapper
from django.conf import settings


class Order(models.Model):
    client = models.ForeignKey(Shopper, on_delete=models.CASCADE)
    payment_details = models.FloatField(max_length=45, default=0)
    order_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.client.username} ({len(self.unit_price)})'

    class Meta:
        verbose_name = 'Commande'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.unit_price
        super().save(*args, **kwargs)

    @property
    def unit_price(self):
        # Récupérer le premier order detail lié à cette commande
        order_details = self.orderdetail_set.all()
        y = 0
        value = [order_detail.unit_price for order_detail in order_details]
        for i in value:
            try:
                y += float(i)
            except:
                pass
        self.payment_details = y
        return value


class OrderDetail(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.CharField(max_length=45, null=True, blank=True)
    unit_price = models.CharField(max_length=45, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.product} ({self.unit_price}$)'

    class Meta:
        verbose_name = 'Detail de commande'
        verbose_name_plural = 'Details des commandes'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.unit_price = float(self.product.price) * float(self.quantity)

        super().save(*args, **kwargs)
        self.order.save(*args, **kwargs)

    # @property
    # def getPrice(self):


class Cart(models.Model):
    # quantity = models.CharField(max_length=45)
    total_price = models.FloatField(max_length=45, null=True, blank=True)
    client = models.ForeignKey(Shopper, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order, blank=True)

    class Meta:
        verbose_name = 'Panier'

    def __str__(self) -> str:
        return f"{self.client.username} ({self.total_price})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        super().save(*args, **kwargs)


class Product(models.Model):

    product_name = models.CharField(max_length=45)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(
        upload_to="img", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produit"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.thumbnail:
            old_path = self.thumbnail.path
            new_path = os.path.join(
                settings.BASE_DIR.parent, 'client/static/', self.thumbnail.name)

            os.makedirs(os.path.dirname(new_path), exist_ok=True)

            os.rename(old_path, new_path)

            self.thumbnail.name = os.path.relpath(
                new_path, settings.BASE_DIR.parent)

            super().save(update_fields=['thumbnail'])

    def __str__(self) -> str:
        return self.product_name


class Invoice(models.Model):
    total_amount = models.CharField(max_length=45, null=True, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.order.client.username

    class Meta:
        verbose_name = "Facture"


class InvoiceDetail(models.Model):
    unit_price = models.IntegerField()
    quantity = models.IntegerField()
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Detail de Facture"
        verbose_name_plural = "Details des Factures"

# class ProductHasCart(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
