from django.shortcuts import get_object_or_404
from rest_framework import exceptions, permissions, viewsets

from api.v1.permissions import ExtendedRights
from api.v1.serializers.review_serializer import ReviewSerilizer
from reviews.models import Review, Title


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerilizer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        ExtendedRights
    )
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_title(self):
        title_id = self.kwargs.get('title_id')
        return get_object_or_404(Title, id=title_id)

    def get_queryset(self):
        title = self.get_title()
        return title.reviews.all()

    def perform_create(self, serializer):
        title = self.get_title()
        user = self.request.user
        serializer.save(author=user, title=title)
