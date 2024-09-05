from rest_framework import filters

from api.v1.permissions import ReadOnlyOrIsAdmin
from api.v1.serializers.genre_serializer import GenreSerializer
from api.v1.mixins import CustomMixin
from reviews.models import Genre


class GenreViewSet(CustomMixin):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (ReadOnlyOrIsAdmin,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
