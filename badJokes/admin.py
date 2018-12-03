from django.contrib import admin

from .models import Badjokes, Players

admin.site.register(Players)
admin.site.register(Badjokes)

# Register your models here.
