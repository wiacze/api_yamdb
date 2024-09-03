from rest_framework import viewsets

from api.v1.filters import TitleFilter
from api.v1.permissions import ReadOnlyOrIsAdmin
from api.v1.serializers.title_serializer import (TitleCreateSerializer,
                                                 TitleSerializer)
from reviews.models import Title


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = (ReadOnlyOrIsAdmin,)
    filterset_class = TitleFilter
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TitleSerializer
        return TitleCreateSerializer
