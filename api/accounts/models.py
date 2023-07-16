from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


# class User(AbstractUser):
#     pass


# class Shopper(models.Model):
#     user = models.OneToOneField(
#         User, on_delete=models.CASCADE, related_name='shopper')
#     groups = models.ManyToManyField(Group, blank=True)
#     user_permissions = models.ManyToManyField(Permission, blank=True)

class Shopper(models.Model):
    name = models.CharField(max_length=45, blank=False, default="")
    email = models.CharField(max_length=45, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
