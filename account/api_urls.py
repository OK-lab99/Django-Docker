from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('profile/', views.ProfileList.as_view(), name='profile_list'),
]