from rest_framework import serializers

from api.v1.serializers.category_serializer import CategorySerializer
from api.v1.serializers.genre_serializer import GenreSerializer
from reviews.models import Title, Genre, Category


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField(read_only=True)
    genre = GenreSerializer(many=True, required=True)
    category = CategorySerializer(required=True)

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'rating',
            'description',
            'genre',
            'category'
        )

    def get_rating(self, obj):
        """Вычисляет среднее значение рейтинга для данного Title."""
        reviews = obj.reviews.all()
        if reviews.exists():
            scores = reviews.values_list('score', flat=True)
            average_rating = round(sum(scores) / len(scores))
            return average_rating
        return None


class TitleCreateSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True,
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all(),
    )

    class Meta:
        model = Title
        fields = ('name', 'year', 'description', 'genre', 'category')

    def to_representation(self, value):
        serializer = TitleSerializer(value)
        return serializer.data
