from django.contrib.contenttypes.models import ContentType
from django.views.generic import DetailView

from cart_app.mixins import CartMixin
from category_app.mixins import CategoryDetailViewMixin
from review_app.models import Review
from .mixins import ProductMixin

from .models import Sport, TV, Toys, Goods


class ProductDetailView(ProductMixin, CartMixin, CategoryDetailViewMixin, DetailView):
    """Отображение информации о товаре"""

    CT_MODEL_CLASS = {
        'sport': Sport,
        'tv': TV,
        'toys': Toys,
        'goods': Goods,
    }

    # вьюшка для обработки сразу нескольких моделей
    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product/product_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        context['ct_model'] = self.model._meta.model_name
        content_type = ContentType.objects.get(model=self.model._meta.model_name).id
        context['reviews'] = Review.objects.filter(content_type=content_type).order_by('-created_at')
        context['cart'] = self.cart
        context['recently_viewed_products'] = self.recently_viewed_products

        return context



