from django.db import models
from main.functions import slugify
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
# Create your models here.


class Goods(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=100, default='Товар')
    slug = models.SlugField(verbose_name='URL:', max_length=255, unique=True, db_index=True)
    description = models.TextField(verbose_name='Описание', max_length=1000, default='', blank=True)
    price = models.IntegerField(verbose_name='Цена', default=999999)
    photo = models.FileField(verbose_name='Фото товара', upload_to='goods/', default='', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['title']

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super().save(force_insert, force_update, using, update_fields)


class Orders(models.Model):
    order_num = models.AutoField(verbose_name='Номер заказа', primary_key=True, unique=True, db_index=True,
                                 editable=False)
    order_owner = models.ForeignKey(User, verbose_name='Имя заказчика', to_field='id', on_delete=models.DO_NOTHING)
    owner_data = models.TextField(verbose_name='Доп. информация', max_length=1000, default='г. Москва, '
                                                                                           'улица Пушкина, '
                                                                                           'дом Колотушкина')
    order_sum = models.IntegerField(verbose_name='Сумма заказа', default=0, editable=False)
    order_key = models.CharField(verbose_name='Ключ заказа', editable=False, max_length=32,
                                 default=get_random_string(length=32))
    processed = models.BooleanField(verbose_name='Обработан', default=False)

    def __str__(self):
        return "Заказ №" + str(self.order_num)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-order_num']


class OrdersData(models.Model):

    order = models.ForeignKey(Orders, to_field='order_num', on_delete=models.RESTRICT, verbose_name='Номер заказа')
    product = models.ForeignKey(Goods, to_field='id', verbose_name='Товар', on_delete=models.RESTRICT)
    quantity = models.IntegerField(verbose_name='Количество', default=1)

    def __str__(self):
        return "Данные заказа №" + str(self.order.order_num)

    class Meta:
        verbose_name = "Данные по заказу"
        verbose_name_plural = "Данные по заказам"
        ordering = ['-order']


class UserCart(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, to_field='id')
    product = models.ForeignKey(Goods, on_delete=models.DO_NOTHING, to_field='id')

    def __str__(self):
        return "Корзина пользователя " + self.user.username

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины пользователей"
