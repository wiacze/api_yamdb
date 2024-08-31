import django_filters
from reviews.models import Title


class TitleFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(
        field_name='category__slug',
        lookup_expr='exact'
    )
    genre = django_filters.CharFilter(
        field_name='genre__slug',
        lookup_expr='exact'
    )
    year = django_filters.NumberFilter(
        lookup_expr='exact'
    )
    name = django_filters.CharFilter(
        lookup_expr='icontains'
    )

    class Meta:
        model = Title
        fields = ['category', 'genre', 'year', 'name']
