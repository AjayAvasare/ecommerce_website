from django.urls import path
from .views import home, add_to_cart, remove_from_cart

urlpatterns = [
    path('', home, name='home'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]
