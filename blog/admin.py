from django.contrib import admin

# Register your models here.
from . import models
from blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')

admin.site.register(Article, ArticleAdmin)


