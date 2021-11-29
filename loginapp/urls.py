from django.urls import path 
from . import views
urlpatterns= [
    path('loginapp/',views.fnlogin,name='loginapp'),
]