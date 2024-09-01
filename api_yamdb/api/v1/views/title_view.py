from rest_framework import mixins, viewsets

from reviews.models import Title
from api.v1.serializers.title_serializer import (TitleSerializer,
                                                 TitleCreateSerializer)
from api.v1.filters import TitleFilter
from api.v1.permissions import ReadOnlyOrIsAdmin


class TitleViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (ReadOnlyOrIsAdmin,)
    filterset_class = TitleFilter
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TitleSerializer
        return TitleCreateSerializer
