from rest_framework import serializers

from reviews.models import Review


class ReviewSerilizer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = (
            'id',
            'text',
            'author',
            'score',
            'pub_date'
        )

    def validate(self, data):
        if self.instance is None:
            user = self.context['request'].user
            title = self.context['view'].kwargs.get('title_id')
            existing_review = Review.objects.filter(
                author=user,
                title=title
            ).exists()

            if existing_review:
                raise serializers.ValidationError(
                    "Вы уже оставили отзыв к этому произведению."
                )

        return data
