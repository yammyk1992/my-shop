from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse

from category_app.models import Category


# аналог get_absolute_url
def get_product_url(obj, viewname):
    # вытягиваем с модели его имя
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        # первые продукты будут выводиться c ...
        with_respect_to = kwargs.get('with_respect_to')
        products = []

        ct_models = ContentType.objects.filter(model__in=args)

        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                print(ct_model, 'CT MODEEEEEL')
                if with_respect_to in args:
                    return sorted(products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to),
                                  reverse=True)
        return products


class Product(models.Model):
    """Товары"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория товара')
    name = models.CharField(max_length=200, verbose_name='Название товара')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')
    image = models.ImageField(upload_to='products/%Y', verbose_name='Картинка товара')
    description = models.TextField(blank=True, null=True, max_length=200, default='', verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара')
    available = models.BooleanField(default=True)

    objects = LatestProductsManager()

    def __str__(self):
        return self.name

    def get_model_name(self):
        return self.__class__.__name__.lower()

    class Meta:
        abstract = True
        verbose_name = 'Все товары'
        verbose_name_plural = 'Все товары'


class Sport(Product):
    """Cпорт товары"""
    kind_of_sport = models.CharField(max_length=200, verbose_name="Вид спорта")
    material = models.CharField(max_length=100, verbose_name="Материал товара")
    colour = models.CharField(max_length=25, verbose_name="Цвет товара")
    country = models.CharField(max_length=30, verbose_name="Страна происхождения")

    def __str__(self):
        return "{} : {}".format(self.category.name, self.name)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    class Meta:
        verbose_name = 'Спортивный товар'
        verbose_name_plural = 'Спортивные товары'


class TV(Product):
    """Телевизоры и видео"""
    diagonal = models.CharField(max_length=200, verbose_name="Диагональ")
    smart_tv = models.BooleanField(default=True)
    release = models.DateTimeField(verbose_name="Выпуск на рынок")
    resolution = models.CharField(max_length=200, verbose_name="Разрешение экрана")

    def __str__(self):
        return "{} : {}".format(self.category.name, self.name)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    class Meta:
        verbose_name = 'Телевизор'
        verbose_name_plural = 'Телевизоры'


class Toys(Product):
    """Игрушки"""
    age = models.IntegerField(verbose_name="Возвраст")
    material = models.CharField(max_length=100, verbose_name="Материал игрушки")
    release = models.DateTimeField(verbose_name="Выпуск на рынок")
    country = models.CharField(max_length=30, verbose_name="Страна происхождения")
    company = models.CharField(max_length=30, verbose_name="Фирма")

    def __str__(self):
        return "{} : {}".format(self.category.name, self.name)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    class Meta:
        verbose_name = 'Игрушка'
        verbose_name_plural = 'Игрушки'


class Goods(Product):
    company = models.CharField(max_length=30, verbose_name="Фирма")
    country = models.CharField(max_length=30, verbose_name="Страна происхождения")
    sex = models.CharField(max_length=10, verbose_name='Пол')
    size = models.IntegerField(verbose_name='Размер')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.name)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

    class Meta:
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'


class ImageSportProducts(models.Model):
    sport_products = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='image_sport_product')
    image = models.ImageField(upload_to='image_product/%Y', null=True, blank=True,
                              verbose_name='Картинка товара')

    class Meta:
        verbose_name = 'Картинка спортивного товара'
        verbose_name_plural = 'Картинки спортивных товаров товаров'


class ImageTVProducts(models.Model):
    tv_products = models.ForeignKey(TV, on_delete=models.CASCADE, related_name='image_tv_product')
    image = models.ImageField(upload_to='image_product/%Y', null=True, blank=True,
                              verbose_name='Картинка товара')

    class Meta:
        verbose_name = 'Картинка телевизора'
        verbose_name_plural = 'Картинки телевизоров'


class ImageToysProducts(models.Model):
    toys_products = models.ForeignKey(Toys, on_delete=models.CASCADE, related_name='image_toys_product')
    image = models.ImageField(upload_to='image_product/%Y', null=True, blank=True,
                              verbose_name='Картинка товара')

    class Meta:
        verbose_name = 'Картинка игрушки'
        verbose_name_plural = 'Картинки игрушек'


class ImageGoodsProducts(models.Model):
    goods_products = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='image_goods_product')
    image = models.ImageField(upload_to='image_product/%Y', null=True, blank=True,
                              verbose_name='Картинка товара')

    class Meta:
        verbose_name = 'Картинка вещей'
        verbose_name_plural = 'Картинки вещей'
