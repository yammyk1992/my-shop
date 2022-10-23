from django.views.generic.detail import SingleObjectMixin
from .models import Category
from product_app.models import Sport, TV, Toys, Goods


class CategoryDetailViewMixin(SingleObjectMixin):
    CATEGORY_SLUG_TO_PRODUCT_MODEL = {
        'sport': Sport,
        'tv': TV,
        'toys': Toys,
        'goods': Goods,

    }

    # вывод контекста в наш шаблон
    def get_context_data(self, *args, **kwargs):
        if isinstance(self.get_object(), Category):
            model = self.CATEGORY_SLUG_TO_PRODUCT_MODEL[self.get_object().slug]
            print(model, "MODEL")
            context = super().get_context_data(**kwargs)
            context['categories'] = Category.objects.get_categories_for_left_sidebar()
            context['category_products'] = model.objects.all()
            return context
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.get_categories_for_left_sidebar()

        return context
