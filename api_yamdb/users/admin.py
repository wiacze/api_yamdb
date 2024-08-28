from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'role',
    )
    search_fields = (
        'role',
        'username',
        'first_name',
        'last_name',
    )
    list_filter = (
        'role',
    )
    list_editable = (
        'role',
    )
    list_display_links = (
        'id',
        'username'
    )
    list_per_page = 10


admin.site.register(User, UserAdmin)
