from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from account import views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login/', views.Login.as_view()),
    path('logout/',LogoutView.as_view()),
    path('blog/',include('blog.urls')),
    path('signup/',views.signup),
    path('mypage/',views.mypage),
    path('contact/',views.contact),
    path('explain/',views.explain),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

