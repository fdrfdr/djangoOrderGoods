from main import views
from django.urls import path, include
from django.contrib.auth.forms import AuthenticationForm


urlpatterns = [
    path('', views.main, name='main'),
    path('catalog', views.catalog, name='catalog'),
    path('signup', views.registration, name='signup'),
    path('add-to-cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('cart', views.get_cart, name='cart'),
    path('make_order', views.make_order, name='make_order'),
    path('order-view', views.order_view, name='order_view'),
    path('catalog/<slug:product_slug>', views.get_product_by_slug, name="product_by_slug"),
    path('', include('django.contrib.auth.urls'))
]
