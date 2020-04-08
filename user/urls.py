from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.Register_user,name='register'),
    path('profile',views.profile,name='profile'),
    path('deleteuser',views.Deleteuser,name='deleteuser'),
    path('registeradmin',views.Register_admin,name='registeradmin'),
]

