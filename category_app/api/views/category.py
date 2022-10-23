from rest_framework import filters
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from category_app.api.serializers.category import CategorySerializer
from category_app.models import Category


class CategoryViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [filters.OrderingFilter]
