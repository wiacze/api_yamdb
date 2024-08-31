from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views.category_view import CategoryViewSet
from api.v1.views.title_view import TitleViewSet


router = DefaultRouter()

router.register('categories', CategoryViewSet, basename='categories')
router.register('titles', TitleViewSet, basename='titles')


urlpatterns = [
    path('', include(router.urls)),
]
