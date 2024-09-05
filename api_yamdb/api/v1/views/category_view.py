from rest_framework import filters, mixins, viewsets

from api.v1.permissions import IsAdminOrReadOnly
from api.v1.serializers.category_serializer import CategorySerializer
from reviews.models import Category


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
