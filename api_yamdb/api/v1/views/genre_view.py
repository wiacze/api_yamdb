from rest_framework import filters, mixins, viewsets

from api.v1.permissions import IsAdminOrReadOnly
from api.v1.serializers.genre_serializer import GenreSerializer
from reviews.models import Genre


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
