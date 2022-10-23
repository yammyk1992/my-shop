from django.shortcuts import render
from django.views import View

from cart_app.mixins import CartMixin
from product_app.models import *


class HomeView(CartMixin, View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_left_sidebar()
        products = Product.objects.get_products_for_main_page('tv', 'toys', 'goods', 'sport',
                                                              with_respect_to='sport')

        context = {
            'categories': categories,
            'products': products,
            'cart': self.cart,
        }
        return render(request, 'base_app/base.html', context)
