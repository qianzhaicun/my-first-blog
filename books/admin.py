from django.contrib import admin

# Register your models here.
from books.models import *
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state_province','country','website')
    list_filter = ('name', 'city', 'country', 'address')
    search_fields = ('name', 'city')

    ordering = ['name', 'country']
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(book)
admin.site.register(Author)
