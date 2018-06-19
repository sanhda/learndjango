from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post')
]
