# Generated by Django 4.2.3 on 2023-07-17 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_cart_options_alter_order_payment_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]