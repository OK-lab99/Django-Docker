from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('article/', views.ArticleList.as_view(), name='article_list'),
    path('comment/', views.CommentList.as_view(), name='comment_list'),
]