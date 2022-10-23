from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .mixins import CartMixin
from category_app.models import Category
from .models import CartProduct
from django.contrib import messages
from .utils import recalculation_cart


class CartView(CartMixin, View):
    """Представление для детализации корзины"""

    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_left_sidebar()
        context = {
            'cart': self.cart,
            'categories': categories
        }
        return render(request, 'cart_app/cart.html', context)


class AddToCartView(CartMixin, View):
    """Представление для добавление товараров в корзину"""

    def get(self, request, *args, **kwargs):
        # распаковываем из словаря нужные нам типы моделей и слаг товара
        ct_model, product_slug = kwargs.pop('ct_model'), kwargs.get('slug')
        # через content_type определяем модель товара
        content_type = ContentType.objects.get(model=ct_model)
        # получаем продукт вызывая у content_type его родительскую модель и через менеджера находим продукт слаг
        product = content_type.model_class().objects.get(slug=product_slug)
        # создаём карт продукт объект с необходимыми аргументами
        cart_product, created = CartProduct.objects.get_or_create(user=self.cart.owner, cart=self.cart,
                                                                  content_type=content_type,
                                                                  object_id=product.id)
        # если уже сработал метод creat, мы просто делаем редирект в корзину!
        if created:
            self.cart.products.add(cart_product)
        # пересчитываем нашу корзину
        recalculation_cart(self.cart)
        # выводим сообщение про действия в корзине
        messages.add_message(request, messages.INFO, f'Товар - {product.name} успешно добавлен')
        return HttpResponseRedirect('/cart/')


class DeleteFromCartView(CartMixin, View):
    """Представление для удаления товаров из корзины"""

    def get(self, request, *args, **kwargs):
        ct_model, product_slug = kwargs.pop('ct_model'), kwargs.get('slug')
        content_type = ContentType.objects.get(model=ct_model)
        product = content_type.model_class().objects.get(slug=product_slug)
        cart_product = CartProduct.objects.get(user=self.cart.owner, cart=self.cart,
                                               content_type=content_type,
                                               object_id=product.id)
        self.cart.products.remove(cart_product)
        # удаляем продукт-корзины из базы данных
        cart_product.delete()
        recalculation_cart(self.cart)
        # выводим сообщение про действия в корзине
        messages.add_message(request, messages.INFO, f'Товар - {product.name} успешно удалён')
        return HttpResponseRedirect('/cart/')


class EditQTYView(CartMixin, View):
    """Представление изменения количества товаров в корзине"""

    def post(self, request, *args, **kwargs):
        ct_model, product_slug = kwargs.pop('ct_model'), kwargs.get('slug')
        content_type = ContentType.objects.get(model=ct_model)
        product = content_type.model_class().objects.get(slug=product_slug)
        cart_product = CartProduct.objects.get(user=self.cart.owner, cart=self.cart,
                                               content_type=content_type,
                                               object_id=product.id)
        qty = int(request.POST.get('qty'))
        cart_product.qty = qty
        cart_product.save()
        recalculation_cart(self.cart)
        # выводим сообщение про действия в корзине
        messages.add_message(request, messages.INFO, 'Количество успешно изменено')
        return HttpResponseRedirect('/cart')
