from django.contrib import admin

from .models import File, Category

admin.site.register(Category)
admin.site.register(File)