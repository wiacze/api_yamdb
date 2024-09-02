from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class SignUpSerializer(serializers.Serializer):

    username = serializers.RegexField(
        regex=r'^[\w.@+-]+$',
        max_length=150,
        required=True
    )
    email = serializers.EmailField(
        max_length=150,
        required=True
    )

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Недопустимое имя пользователя.'
            )
        return value

    def validate(self, data):
        item = ''
        message = f'Пользователь с таким {item} уже существует.'
        if User.objects.filter(username=data['username']).exists():
            user = User.objects.get(username=data['username'])
            if user.email != data['email']:
                item = 'username'
                raise serializers.ValidationError(message)
        if User.objects.filter(email=data['email']).exists():
            user = User.objects.get(email=data['email'])
            if user.username != data['username']:
                item = 'email'
                raise serializers.ValidationError(message)
        return data


class GetTokenSerializer(serializers.Serializer):
    username = serializers.RegexField(
        regex=r'^[\w.@+-]+$',
        max_length=150,
        required=True
    )
    confirmation_code = serializers.CharField(
        max_length=150,
        required=True
    )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )
