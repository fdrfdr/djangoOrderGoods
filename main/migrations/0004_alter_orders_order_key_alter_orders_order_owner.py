# Generated by Django 4.2.8 on 2023-12-27 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_alter_orders_order_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_key',
            field=models.CharField(default='e9OmtoM1KTd7BtyO73CQ93ROsRvOkefa', editable=False, max_length=32, verbose_name='Ключ заказа'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Имя заказчика'),
        ),
    ]
