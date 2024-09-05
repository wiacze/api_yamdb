from rest_framework import filters

from api.v1.mixins import CustomMixin
from api.v1.permissions import ReadOnlyOrIsAdmin
from api.v1.serializers.category_serializer import CategorySerializer
from reviews.models import Category


class CategoryViewSet(CustomMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (ReadOnlyOrIsAdmin,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
