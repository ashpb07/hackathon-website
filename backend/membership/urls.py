from django.urls import path,include
from . import views

urlpatterns = [
 path('signup/',views.singup,name='signup'),
 path('signin/',views.singin,name='signin'),
 path('signout/',views.logout,name='signout'),


]
