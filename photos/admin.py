from django.contrib import admin
from .models import Category,Photo,Location
# Register your models here.
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Location)