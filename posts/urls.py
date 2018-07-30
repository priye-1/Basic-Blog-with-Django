# coding=utf-8
from . import views
from django.urls import path

app_name = "posts"

urlpatterns = [
    path('', views.index, name="index"),
    path('post-list/', views.postList, name="post-list"),
    path('all-authors/', views.all_authors, name="all-authors"),
    path('results/', views.search, name="search"),
    path('new/', views.create, name="post-create"),
    path('<int:post_id>/', views.detail, name="post-detail"),
    path('edit/<int:post_id>/', views.edit, name="post-edit"),
    path('update/<int:post_id>/', views.update, name="post-update"),
    path('delete/<int:post_id>/', views.delete, name="post-delete"),
    path('post-list/templates/', views.byAuthor, name="post-authors")
]
