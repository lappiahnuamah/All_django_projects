from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ['todo', 'is_completed', 'date_published']

admin.site.register(Todo, TodoAdmin)