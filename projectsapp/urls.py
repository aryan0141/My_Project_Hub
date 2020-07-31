from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('feedback', views.feedback, name='feedback'),
    path('chatter_bot', views.chatter_bot, name='chatter_bot'),
]