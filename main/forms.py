from django import forms

from main.models import Goods, Orders


class ProductForm(forms.ModelForm):

    class Meta:
        model = Goods
        fields = ['title', 'photo', 'description', 'price']


class OrderViewForm(forms.ModelForm):

    class Meta:
        model = Orders
        fields = ['order_num', 'order_key']
