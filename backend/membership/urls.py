from django.urls import path,include
from . import views

urlpatterns = [
 path('signup/',views.singup,name='index'),
 path('signin/',views.singin,name='index'),
 path('signout/',views.logout,name='signout'),


]
