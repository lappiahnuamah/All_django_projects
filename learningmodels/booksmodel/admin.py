from django.contrib import admin

# Register your models here.
from booksmodel.models import Book, Vehicle

class BookAdmin(admin.ModelAdmin):
    list_display = ['bookTitle', 'bookAuthor', 'publisher', 'timestamp']


class VehicleAdmin(admin.ModelAdmin):
    list_display = ['vehicle_registration_number', 'vehicle_brand', 'vehicle_color', 'vehicle_manufactured']

admin.site.register(Book, BookAdmin)
admin.site.register(Vehicle, VehicleAdmin)