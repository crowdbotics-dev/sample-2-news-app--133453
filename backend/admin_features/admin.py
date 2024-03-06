from django.contrib import admin
from .models import ContentModeration, UserManagement

admin.site.register(ContentModeration)
admin.site.register(UserManagement)

# Register your models here.
