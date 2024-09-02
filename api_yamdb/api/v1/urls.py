from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views.category_view import CategoryViewSet
from api.v1.views.title_view import TitleViewSet
from api.v1.views.genre_view import GenreViewSet
from api.v1.views.user_view import SignUpViewSet, GetTokenViewSet, UserViewSet


router = DefaultRouter()

router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')
router.register('users', UserViewSet, basename='users')

auth_urls = [
    path(
        'signup/', SignUpViewSet.as_view({'post': 'create'}), name='signup'
    ),
    path(
        'token/', GetTokenViewSet.as_view({'post': 'create'}), name='token'
    ),
]

urlpatterns = [
    path('auth/', include(auth_urls)),
    path('', include(router.urls)),
]
