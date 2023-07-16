from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Shopper(AbstractUser):
    pass

# class Shopper(models.Model):
#     name = models.CharField(max_length=45, blank=False, default="")
#     email = models.CharField(max_length=45, null=True, blank=True)
#     phone_number = models.IntegerField(null=True, blank=True)
