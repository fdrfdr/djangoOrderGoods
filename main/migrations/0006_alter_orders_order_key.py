# Generated by Django 4.2.8 on 2023-12-27 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_orders_data_ordersdata_alter_orders_order_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_key',
            field=models.CharField(default='eS7OntggAnSGiHccj11CO4K67AO7PKTR', editable=False, max_length=32, verbose_name='Ключ заказа'),
        ),
    ]
