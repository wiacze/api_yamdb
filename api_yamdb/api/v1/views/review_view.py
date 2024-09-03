from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from reviews.models import Title, Review
from api.v1.serializers.review_serializer import ReviewSerilizer
from api.v1.permissions import ExtendedRights


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerilizer
    permission_classes = (ExtendedRights, IsAuthenticatedOrReadOnly)
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
        if Review.objects.filter(author=user, title=title).exists():
            raise ValidationError(
                {'detail': 'Вы уже оставляли отзыв на это произведение.'}
            )
        serializer.save(author=user, title=title)
