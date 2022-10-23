from rest_framework import filters
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from review_app.api.serializers.review import ReviewSerializer
from review_app.models import Review


class ReviewViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    filter_backends = [filters.OrderingFilter]
