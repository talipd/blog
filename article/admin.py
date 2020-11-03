from django.contrib import admin

from .models import Article,Comment
# Register your models here.
# admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display =["title","author","created_data"]
    list_display_links=["title","author","created_data"]
    list_filter = ["author","created_data"]
    ordering = ["created_data","title","author"]
    search_fields = ["title"]
    class Meta:
        model=Article

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display =["article_id","comment_title","comment_author","comment_created"]
    list_display_links=["comment_title","comment_author","comment_created"]
    list_filter = ["comment_author","comment_created"]
    ordering = ["comment_created","comment_title","comment_author"]
    search_fields = ["comment_title"]
    class Meta:
        model=Comment

