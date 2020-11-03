from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title=models.CharField(max_length = 50, verbose_name="Başlık")
    content=RichTextField()
    created_data=models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank = True,null = True, verbose_name="Resim Ekle")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_data']    
class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="makale",related_name="comments")
    comment_author=models.CharField(max_length = 15, verbose_name="Yorum Yapan")
    comment_title=models.CharField(max_length = 50, verbose_name="Yorum Başlık")
    comment_content=models.CharField(max_length = 250, verbose_name="Yorum İçerik")
    comment_created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_title
    class Meta:
        ordering = ['-comment_created'] 