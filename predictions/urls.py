from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict_genre/', views.predict_genre, name='predict_genre'),
]
