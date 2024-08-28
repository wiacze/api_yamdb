from django.contrib import admin

from reviews.models import Category, Genre, Title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'description')
    filter_horizontal = ('genre',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
