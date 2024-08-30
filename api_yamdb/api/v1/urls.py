from django.urls import include, path
from rest_framework.routers import DefaultRouter

from v1.views.category_view import CategoryViewSet


router_v1 = DefaultRouter()

router_v1.register('categories', CategoryViewSet, basename='categories')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
