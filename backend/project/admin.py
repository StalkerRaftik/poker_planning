# from django.contrib import admin
# from .models import Genre, Anime, Rating
#
#
# @admin.register(Genre)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')
#
#
# @admin.register(Anime)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('original_name', 'name', 'premiere_date', 'status')
#     list_filter = ('premiere_date', 'status')
#     ordering = ('-premiere_date',)
#
#
# @admin.register(Rating)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('owner', 'anime', 'value')
#     list_filter = ('owner', 'anime')
