from django.contrib import admin
from .models import Todo

# Register your models here.
class todoAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'date','completed')
    list_display_links = ('id', 'title')
admin.site.register(Todo, todoAdmin)
