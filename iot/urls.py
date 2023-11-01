from django.contrib import admin
from django.urls import path, include

from iot import views

urlpatterns = [
    path('main', views.index),
    path('fire', views.fire),
    path('robber', views.robber),
    path('accident', views.accident),
]
