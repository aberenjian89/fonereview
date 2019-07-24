from django.contrib import admin
from .models import (
    Device,
    Comment,
    Rate
)
# Register your models here.

admin.site.register(Device)
admin.site.register(Comment)
admin.site.register(Rate)