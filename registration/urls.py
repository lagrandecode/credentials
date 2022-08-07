
from django.urls import path
from . import views

urlpatterns = [
    path('', views.registerview, name='register'),
    path('login', views.loginview, name='login')
]
