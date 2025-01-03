from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers

from api_yamdb.constants import REGEX, USERFIELDS_LENGTH, EMAIL_LENGTH


User = get_user_model()


class SignUpSerializer(serializers.Serializer):

    username = serializers.RegexField(
        regex=REGEX,
        max_length=USERFIELDS_LENGTH,
        required=True,
    )
    email = serializers.EmailField(
        max_length=EMAIL_LENGTH,
        required=True,
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
        username = data['username']
        email = data['email']

        user = User.objects.filter(
            Q(username=username) | Q(email=email)).first()

        if user and user.email != email:
            raise serializers.ValidationError(
                'Пользователь с таким именем уже существует.'
            )
        if user and user.username != username:
            raise serializers.ValidationError(
                'Пользователь с такой почтой уже существует.'
            )
        return data


class GetTokenSerializer(serializers.Serializer):
    username = serializers.RegexField(
        regex=REGEX,
        max_length=USERFIELDS_LENGTH,
        required=True,
    )
    confirmation_code = serializers.CharField(
        max_length=USERFIELDS_LENGTH,
        required=True,
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
            'role',
        )
