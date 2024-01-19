import json

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.core.exceptions import PermissionDenied
# Create your views here.
from main.models import Goods, Orders, OrdersData, UserCart


def main(request):
    context = {
        'auth': request.user.username
    }
    return render(request, 'main/index.html', context)


def catalog(request):
    goods_objects = Goods.objects.all()
    context = {
        'auth': request.user.username,
        'goods': goods_objects
    }
    return render(request, 'main/catalog.html', context)


def registration(request):
    context = {
        'auth': request.user.username
    }
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            context['form'] = form
    else:
        form = UserCreationForm()
        context['form'] = form
    return render(request, 'registration/signup.html', context)


def get_product_by_slug(request, product_slug):
    product = get_object_or_404(Goods, slug=product_slug)
    context = {
        'auth': request.user.username,
        'product': product
    }
    return render(request, 'main/product_view.html', context)


def add_to_cart(request, product_id):
    if request.POST and request.user.is_authenticated:
        redirect_to = request.POST['redirect']
        user = get_object_or_404(User, id=request.user.id)
        product = get_object_or_404(Goods, id=product_id)
        UserCart.objects.create(user=user, product=product)
        return redirect(redirect_to)
    return redirect('catalog')


def get_cart(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        cart_data = UserCart.objects.filter(user=user)
        inner_data = {}
        total_sum = 0
        for product in cart_data:
            value = inner_data.get(str(product.product.id), 0)
            inner_data[str(product.product.id)] = value + 1
            total_sum += product.product.price
        context = {
            'auth': request.user.username,
            'goods': cart_data,
            'cart_data': str(inner_data),
            'total_sum': total_sum
        }
        return render(request, 'main/cart.html', context)
    else:
        raise PermissionDenied()


def make_order(request):
    if request.POST and request.user.is_authenticated:
        json_goods = json.loads(request.POST['cart_data'].replace("'", '"'))
        user = get_object_or_404(User, id=request.user.id)
        order = Orders.objects.create(order_owner=user, order_sum=999999)
        total_price = 0
        for key in json_goods.keys():
            product = get_object_or_404(Goods, id=int(key))
            order_data = OrdersData.objects.create(order=order, product=product, quantity=json_goods[key])
            cart_products = UserCart.objects.filter(user=user, product=product)
            for cart_product in cart_products:
                cart_product.delete()
            total_price += product.price * json_goods[key]
            order.order_sum = total_price
        order.save(update_fields=('order_sum',))
        context = {
            'auth': request.user.username,
            'order': order
        }
        return render(request, 'main/order_result.html', context)
    else:
        raise PermissionDenied()


def order_view(request):
    if request.POST:
        order = get_object_or_404(Orders,
                                  order_num=request.POST['order_num'],
                                  order_key=request.POST['order_key'])
        order_data = OrdersData.objects.filter(order=order)
        context = {
            'order': order,
            'order_data': order_data,
            'auth': request.user.username
        }
        return render(request, 'main/order_view.html', context)
    context = {
        'auth': request.user.username
    }
    return render(request, 'main/order_view.html', context)


def custom_403_view(request, exception):
    return render(request, '403.html')
