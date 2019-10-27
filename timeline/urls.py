from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeline, name='timeline'),
    path('post/<int:pk>/', views.post, name='post'),
    path('post/upload', views.post_upload, name='post_upload'),
]