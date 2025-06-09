from django.contrib import admin
from django.urls import path
from myprofile import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('projects/', views.projects),
]
 