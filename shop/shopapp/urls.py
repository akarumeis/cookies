from django.urls import path
from . views import product_page, basket

urlpatterns = [
    path('', product_page, name='product_page'),
    path('basket/', basket, name='basket')
]
