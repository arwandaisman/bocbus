from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .views import registerView

urlpatterns = [
    path('', registerView, name='registerView'),
]