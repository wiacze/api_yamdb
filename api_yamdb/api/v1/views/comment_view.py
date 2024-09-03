from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404

from reviews.models import Review
from api.v1.permissions import ExtendedRights
from api.v1.serializers.comment_serializer import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, ExtendedRights)
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_review(self):
        review_id = self.kwargs['review_id']
        return get_object_or_404(Review, id=review_id)

    def get_queryset(self):
        return self.get_review().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, review=self.get_review())
