from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from profile_app.models import Profile


class Cart(models.Model):
    """Корзина"""
    owner = models.ForeignKey(Profile, null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField('CartProduct', blank=True, verbose_name='Продукты', related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0, verbose_name="Количество товаров в корзине")
    final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Окончательная цена')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return f'{str(self.id)} - {self.owner}'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartProduct(models.Model):
    """Модель корзины с продуктами"""
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Покупатель', null=True)
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1, verbose_name='Количество')
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.content_object.name)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.content_object.price
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Корзина с продуктами'
        verbose_name_plural = 'Корзина с продуктами'
