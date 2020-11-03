
from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "article"

urlpatterns = [

    path('dashboard/', views.dashboard,name="dashboard"),
    path('addarticle/', views.addArticle,name="addarticle"),
    path('article/<int:id>', views.detail,name="detail"),
    path('update/<int:id>', views.update,name="update"),
    path('delete/<int:id>', views.delete,name="delete"),
    path('', views.article,name="article"),
    path('comment/<int:id>', views.addComment,name="addcomment"),


]
