from django.contrib import admin

# Register your models here.
from . models import photo
admin.site.register(photo)
from . models import team
admin.site.register(team)
