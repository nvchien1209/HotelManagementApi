from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Hotel)
admin.site.register(models.Room)
admin.site.register(models.RoomType)
