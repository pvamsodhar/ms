from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweetList, name='index'),
    path('create/', views.tweetCreate, name='tweetCreate'),
    path('edit/<int:pk>/', views.tweetEdit, name='tweetEdit'), 
    path('delete/<int:pk>/', views.tweetDelete, name='tweetDelete'),
    path('search/', views.search, name='search'),
]
