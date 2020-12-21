from django.urls import path
from django.contrib import admin
from django.shortcuts import render
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.user, name='user'),
    path('tabel/', views.tabel, name='tabel'),
    path('icon/', views.icon, name='icon'),
    path('typo/', views.typo, name='typo'),
    path('<id>/detail',views.detail, name='detail'),
    path('<id>/hapus',views.hapus, name='hapus'),
    path('<id>/edit',views.edit, name='edit'),
    path('profil/', views.profil, name='profil'),

]
