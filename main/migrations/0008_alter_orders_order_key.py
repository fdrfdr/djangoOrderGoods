# Generated by Django 4.2.8 on 2023-12-28 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_good_ordersdata_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_key',
            field=models.CharField(default='ApFJRX0cr51gG28YD7OFBOP0vetAqOz1', editable=False, max_length=32, verbose_name='Ключ заказа'),
        ),
    ]
