from django.shortcuts import render
from .models import Product
# Create your views here.


def product_page(request):
    response = render(request, 'shop.html', context={
                      'title': "Головна", 'text_btn': 'Buy', 'products': Product.objects.all()})
    if request.method == 'POST':
        basket = request.COOKIES.get('cart', None)
        product_id = request.POST.get('id')
        if basket != None:
            basket_list = basket.split(' ')
            if product_id in basket_list:
                pass
            else:
                response.set_cookie('cart', basket+' '+product_id)
        else:
            response.set_cookie('cart', product_id)

    return response


def basket(request):
    context = {
        'title': "Корзина",
        'text_btn': 'Delete'
    }
    basket = []
    basket_cookie = request.COOKIES.get('cart', None)
    if basket_cookie != None:
        
        basket_cookie = basket_cookie.split()
        for product in basket_cookie:
            product = Product.objects.get(pk=product)
            basket.append(product)

    context['products'] = basket

    response = render(request, 'basket.html', context)
    
    if request.method == 'POST':
        basket_cookie = request.COOKIES.get('cart', None)
        basket_cookie = basket_cookie.split()
        product_id = request.POST.get('id')
        basket_cookie.remove(product_id)
        basket_cookie = ' '.join(basket_cookie)
        response.set_cookie('cart', basket_cookie)

    return response
