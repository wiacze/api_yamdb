from enum import Enum


class Role(Enum):
    """Класс-перечисление пользовательских ролей."""

    user = 'user'
    moderator = 'moderator'
    admin = 'admin'

    @classmethod
    def selection(cls):
        return tuple((role.name, role.value) for role in cls)

    @classmethod
    def max_length(cls):
        return max(len(role.value) for role in cls)
