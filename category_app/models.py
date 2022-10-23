from django.db import models

from django.urls import reverse


# функция для аннотации Count - Категорий
def get_models_for_count(*model_names):
    return [models.Count(model_name) for model_name in model_names]


class CategoryManager(models.Manager):

    CATEGORY_NAME_COUNT_NAME = {
        'Sport': 'sport__count',
        'TV': 'tv__count',
        'Toys': 'toys__count',
        'Goods': 'goods__count',

    }

    def get_queryset(self):
        return super().get_queryset()

    def get_categories_for_left_sidebar(self):

        models = get_models_for_count('sport', 'tv', 'toys', 'goods')
        qs = list(self.get_queryset().annotate(*models))
        data = [
            dict(name=c.name, url=c.get_absolute_url(), count=getattr(c, self.CATEGORY_NAME_COUNT_NAME[c.name]))
            for c in qs
        ]
        return data


class Category(models.Model):
    """Категории товаров"""
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
