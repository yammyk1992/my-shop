from django.contrib import messages
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View

from cart_app.mixins import CartMixin
from category_app.models import Category
from profile_app.models import Profile
from .forms import OrderForm


class OrderView(CartMixin, View):
    """Представление для детализации корзины"""

    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_left_sidebar()
        form = OrderForm(request.POST or None)
        context = {
            'cart': self.cart,
            'categories': categories,
            'form': form
        }
        return render(request, 'order/checkout.html', context)


class MakeOrderView(CartMixin, View):
    """Представление для подтверждения оформления заказа"""

    # проверка на правильность заполнения формы
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.customer = Profile.objects.get(user=request.user)
            new_order.first_name = form.cleaned_data['first_name']
            new_order.last_name = form.cleaned_data['last_name']
            new_order.phone = form.cleaned_data['phone']
            new_order.address = form.cleaned_data['address']
            new_order.buying_type = form.cleaned_data['buying_type']
            new_order.order_date = form.cleaned_data['order_date']
            new_order.comment = form.cleaned_data['comment']
            new_order.save()
            self.cart.in_order = True
            self.cart.save()
            new_order.cart = self.cart
            messages.add_message(request, messages.INFO, 'Cпасибо за заказ')

            return HttpResponseRedirect('/')

        return HttpResponseRedirect('/checkout/')


