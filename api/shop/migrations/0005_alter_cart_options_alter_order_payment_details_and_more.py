# Generated by Django 4.2.3 on 2023-07-17 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_cart_total_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Panier'},
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_details',
            field=models.FloatField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
