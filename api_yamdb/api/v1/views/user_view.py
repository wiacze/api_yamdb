from rest_framework import status, mixins, viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator

from api.v1.utils import send_confirmation_code
from api.v1.permissions import IsAdmin
from api.v1.serializers.user_serializer import (
    User, UserSerializer, GetTokenSerializer, SignUpSerializer
)


class SignUpViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, created = self.get_queryset().get_or_create(
            **serializer.validated_data
        )
        confirmation_code = default_token_generator.make_token(user)
        send_confirmation_code(
            email=user.email,
            confirmation_code=confirmation_code,
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetTokenViewSet(mixins.CreateModelMixin,
                      viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = GetTokenSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        confirmation_code = serializer.validated_data.get('confirmation_code')
        user = get_object_or_404(self.get_queryset(), username=username)
        if not default_token_generator.check_token(user, confirmation_code):
            message = {'confirmation_code': 'Невалидный код подтверждения'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        message = {'token': str(AccessToken.for_user(user))}
        return Response(message, status=status.HTTP_200_OK)


class UserViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)

    def get_user(self, username):
        return get_object_or_404(self.get_queryset(), username=username)

    @action(
        detail=False,
        methods=['get'],
        url_path=r'(?P<username>[\w.@+-]+)',
        name='Get user',
    )
    def user(self, request, username):
        serializer = self.get_serializer(self.get_user(username=username))
        return Response(serializer.data, status=status.HTTP_200_OK)

    @user.mapping.patch
    def patch_user(self, request, username):
        serializer = self.get_serializer(
            self.get_user(username=username),
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @user.mapping.delete
    def delete_user(self, request, username):
        self.get_user(username=username).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=False,
        methods=['get'],
        url_path='me',
        permission_classes=(permissions.IsAuthenticated,),
        name='Get me data',
    )
    def me_data(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @me_data.mapping.patch
    def patch_me_data(self, request):
        serializer = self.get_serializer(
            request.user,
            data=request.data,
            partial=True,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(role=request.user.role)
        return Response(serializer.data, status=status.HTTP_200_OK)
