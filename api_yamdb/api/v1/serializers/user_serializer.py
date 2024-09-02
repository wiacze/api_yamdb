from rest_framework import serializers
from django.contrib.auth import get_user_model

from api_yamdb.constants import REGEX, USERFIELDS_LENGTH, EMAIL_LENGTH


User = get_user_model()


class SignUpSerializer(serializers.Serializer):

    username = serializers.RegexField(
        regex=REGEX,
        max_length=USERFIELDS_LENGTH,
        required=True
    )
    email = serializers.EmailField(
        max_length=EMAIL_LENGTH,
        required=True
    )

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Недопустимое имя пользователя.'
            )
        return value

    def validate(self, data):
        """
        Проверяет наличие пользователей, соответствующих введенным данным.
        При совпадении проверяет, что оба поля принадлежат одному пользователю.
        """
        field = ''
        message = f'Пользователь с таким {field} уже существует.'
        #  Если есть пользователь с таким юзернеймом.
        if User.objects.filter(username=data['username']).exists():
            user = User.objects.get(username=data['username'])
            #  Если введенный адрес не совпадает с адресом пользователя.
            if user.email != data['email']:
                field = 'username'
                raise serializers.ValidationError(message)
        #  Если есть пользователь с таким адресом.
        if User.objects.filter(email=data['email']).exists():
            user = User.objects.get(email=data['email'])
            #  Если введенный юзернейм не совпадает с юзернеймом пользователя.
            if user.username != data['username']:
                field = 'email'
                raise serializers.ValidationError(message)
        return data


class GetTokenSerializer(serializers.Serializer):
    username = serializers.RegexField(
        regex=REGEX,
        max_length=USERFIELDS_LENGTH,
        required=True
    )
    confirmation_code = serializers.CharField(
        max_length=USERFIELDS_LENGTH,
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
