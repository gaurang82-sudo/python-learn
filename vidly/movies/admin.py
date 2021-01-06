from django.contrib import admin
from .models import Genre, movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class MovieAdmin(admin.ModelAdmin):
    exclude = ("date_created",)
    list_display = ('title', 'number_in_stock',
                    'daily_rate', 'release_year')


admin.site.register(Genre, GenreAdmin)
admin.site.register(movie, MovieAdmin)


# Register your models here.
