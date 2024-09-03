from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from api.v1.serializers.comment_serializers import CommentSerializer
from api.v1.permissions import ExtendedRights
from reviews.models import Review


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        ExtendedRights, permissions.IsAuthenticatedOrReadOnly
    )
    http_method_names = ('get', 'post', 'patch', 'delete')

    def get_review(self):
        review_id = self.kwargs.get('review_id')
        title_id = self.kwargs.get('title_id')

        return get_object_or_404(Review, pk=review_id, title_id=title_id)

    def get_queryset(self):
        return self.get_review().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, review=self.get_review())
