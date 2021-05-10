from django.db import models

# Create your models here.
# Create your models here.
class Book(models.Model):
    bookTitle = models.CharField(max_length=124)
    bookAuthor = models.CharField(max_length=64)
    publisher = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bookTitle


BRAND = (
    ('HN', 'Honda'),
    ('TY', 'Toyata'),
    ('MD', 'Mercedes'),
    ('BMW', 'BMW'),

)

class Vehicle(models.Model):
    vehicle_registration_number = models.CharField(max_length=16, blank=False)
    vehicle_color               = models.CharField(max_length=128)
    vehicle_image               = models.ImageField(upload_to='media/')
    vehicle_brand               = models.CharField(max_length=32, choices=BRAND)
    vehicle_manufactured        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_registration_number