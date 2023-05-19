from django.contrib import admin
from django.urls import path

from .views import index, profile

app_name = 'product'

urlpatterns = [
    path('', index, name='index'),
    path('profile/<username>', profile, name='profile')
]