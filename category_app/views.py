from django.views.generic import DetailView

from cart_app.mixins import CartMixin

from .mixins import CategoryDetailViewMixin
from .models import Category


class CategoryDetailView(CartMixin, CategoryDetailViewMixin, DetailView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category/category_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart
        return context
