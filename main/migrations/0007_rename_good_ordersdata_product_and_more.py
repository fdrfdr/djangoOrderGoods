# Generated by Django 4.2.8 on 2023-12-27 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_orders_order_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordersdata',
            old_name='good',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_key',
            field=models.CharField(default='M3mz0D3i0G4QzthRmua66gqN4nKOGuFZ', editable=False, max_length=32, verbose_name='Ключ заказа'),
        ),
    ]