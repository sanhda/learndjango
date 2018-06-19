from django.contrib import admin
from .models import Post
from.models import Person
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'shirt_size']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Post, PostAdmin)
admin.site.register(Person, PersonAdmin)
