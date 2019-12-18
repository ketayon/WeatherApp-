from django.contrib import admin
from .models import Bb

# Register your models here.
class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_display_links = ('title')
    search_fields = ('title')

admin.site.register(Bb)