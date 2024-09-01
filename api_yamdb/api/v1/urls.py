from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views.user_view import (UserViewSet,
                                    GetTokenViewSet,
                                    UserCreateViewSet)


router_v1 = DefaultRouter()

router_v1.register('users', UserViewSet, basename='users')

auth_urls = [
    path(
        'signup/', UserCreateViewSet.as_view({'post': 'create'}), name='signup'
    ),
    path(
        'token/', GetTokenViewSet.as_view({'post': 'create'}), name='token'
    ),
]

urlpatterns = [
    path('auth/', include(auth_urls)),
    path('', include(router_v1.urls)),
]
