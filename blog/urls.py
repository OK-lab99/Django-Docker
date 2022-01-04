from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index),
    path('tags/<str:name>/', views.tags),
    path('<int:pk>/',views.article),
    path('post/', views.posts),
]
