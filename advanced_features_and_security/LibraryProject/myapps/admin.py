from django.contrib import admin
from .models import Article
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')
    search_fields = ('title', 'body')

# (Optional) Show groups in admin - Django already provides this, but keep for reference
admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
