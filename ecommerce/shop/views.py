from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem

def home(request):
    products = Product.objects.all()
    cart_items = CartItem.objects.all()
    return render(request, 'shop/home.html', {'products': products, 'cart_items': cart_items})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('home')

def remove_from_cart(request, item_id):
    CartItem.objects.filter(id=item_id).delete()
    return redirect('home')
