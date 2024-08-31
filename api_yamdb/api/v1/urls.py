from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views.category_view import CategoryViewSet
from api.v1.views.genre_view import GenreViewSet


router_v1 = DefaultRouter()

router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')


urlpatterns = [
    path('', include(router_v1.urls)),
]
