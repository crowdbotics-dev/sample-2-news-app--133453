from django.contrib import admin
from .models import Article, Category, Topic

admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Article)

# Register your models here.
