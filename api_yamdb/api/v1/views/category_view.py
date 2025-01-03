from rest_framework import filters

from api.v1.mixins import CreateDestroyListMixin
from api.v1.permissions import IsAdminOrReadOnly
from api.v1.serializers.category_serializer import CategorySerializer
from reviews.models import Category


class CategoryViewSet(CreateDestroyListMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
