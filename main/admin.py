from django.contrib import admin
from main.models import Orders, Goods, OrdersData, UserCart
from django.utils.crypto import get_random_string

# Register your models here.


class AdminGoods(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("title",)}


class AdminOrders(admin.ModelAdmin):

    readonly_fields = ('order_sum', 'order_key')

    def get_changeform_initial_data(self, request):
        return {
            'order_key': get_random_string(length=32),
            'processed': True
        }


admin.site.register(Goods, AdminGoods)
admin.site.register(Orders, AdminOrders)
admin.site.register(OrdersData)

