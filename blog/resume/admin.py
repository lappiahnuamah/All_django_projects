from django.contrib import admin
from .models import Resume , Post, ContactForm
# Register your models here.
admin.site.register(Resume)
admin.site.register(Post)
admin.site.register(ContactForm)