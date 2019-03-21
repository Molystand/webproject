from django.contrib import admin
from news.models import News, Tag, Comment

admin.site.register(News)
admin.site.register(Tag)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'news', 'publish_date']


admin.site.register(Comment, CommentAdmin)
