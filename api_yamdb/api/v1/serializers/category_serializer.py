from rest_framework import serializers

from reviews.models import Category


class CategorySerializer(serializers.ModelSerializer):
    lookup_field = 'slug'  # Для поиска объекта в БД будет поле slug

    class Meta:
        model = Category
        fields = ('name', 'slug')


class CategoryRelatedField(serializers.SlugRelatedField):
    """Полностью настраиваемое реляционное поле, которое точно описывает,
    как выходное представление должно быть сгенерировано из экземпляра модели.
    """

    def to_representation(self, value):
        serializer = CategorySerializer(value)
        return serializer.data
