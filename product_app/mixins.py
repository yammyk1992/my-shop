from django.views import View


from product_app.models import Sport


class ProductMixin(View):
    """Миксин для вывода последних просмотренных товаров через Session"""

    def dispatch(self, request, *args, **kwargs):

        product_slug = kwargs.get('slug')

        recently_viewed_products = None

        if 'recently_viewed' in request.session:

            if product_slug in request.session['recently_viewed']:
                request.session['recently_viewed'].remove(product_slug)

            recently_viewed_products = Sport.objects.filter(slug__in=request.session['recently_viewed'])
            request.session['recently_viewed'].insert(0, product_slug)

            if len(request.session['recently_viewed']) > 5:
                request.session['recently_viewed'].pop()
        else:
            request.session['recently_viewed'] = [product_slug]

        request.session.modified = True

        self.recently_viewed_products = recently_viewed_products

        return super().dispatch(request, *args, **kwargs)



