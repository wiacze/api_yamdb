from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404

from reviews.models import Title
from api.v1.serializers.review_serializer import ReviewSerializer
from api.v1.permissions import ExtendedRights


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, ExtendedRights
    )
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_title(self):
        title_id = self.kwargs['title_id']
        return get_object_or_404(Title, id=title_id)

    def get_queryset(self):
        return self.get_title().reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title())
