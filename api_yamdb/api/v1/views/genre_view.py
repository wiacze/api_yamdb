from rest_framework import filters, mixins, viewsets

from reviews.models import Genre
from api.v1.serializers.genre_serializer import GenreSerializer
from api.v1.permissions import ReadOnlyOrIsAdmin


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (ReadOnlyOrIsAdmin,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
