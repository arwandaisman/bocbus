from django.urls import path
from django.contrib import admin
from django.shortcuts import render
from . import views


urlpatterns = [
    path('',views.index),
    path('<id>/detail/', views.detail, name='detail'),
    path('tambah/', views.tambah, name='tambah'),
    path('pesan/', views.pesan, name='pesan'),

]