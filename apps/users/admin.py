from django.contrib import admin

from .models import Film,User,UserMovie

admin.site.register(Film)
admin.site.register(User)
admin.site.register(UserMovie)
