from rest_framework import filters, mixins, viewsets

from reviews.models import Title
from api.v1.serializers.title_serializer import TitleSerializer, TitleCreateSerializer


class TitleViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = ()
    filter_backends = (filters.SearchFilter,)
    filterset_fields = {
        'category': ['slug'],  # Filter by category slug
        'genre': ['slug'],  # Filter by genre slug
        'name': ['icontains'],  # Case-insensitive search by name
        'year': ['exact']  # Exact match for year
    }

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TitleSerializer
        return TitleCreateSerializer
