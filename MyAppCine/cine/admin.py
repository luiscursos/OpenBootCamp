from django.contrib import admin
from .models import Genre, Movie, Film_director, WhereSeeMovie

# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Film_director)
admin.site.register(WhereSeeMovie)
