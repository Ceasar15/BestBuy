# Generated by Django 3.1.5 on 2022-01-15 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
    ]