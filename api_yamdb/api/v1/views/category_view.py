from rest_framework import filters, mixins, viewsets

from reviews.models import Category
from api.v1.serializers.category_serializer import CategorySerializer
from api.v1.permissions import ReadOnlyOrIsAdmin


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (ReadOnlyOrIsAdmin,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
