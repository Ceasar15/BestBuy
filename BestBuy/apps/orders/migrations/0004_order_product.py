# Generated by Django 3.1.5 on 2022-01-15 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_tags'),
        ('orders', '0003_auto_20210121_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_order', to='products.product'),
        ),
    ]