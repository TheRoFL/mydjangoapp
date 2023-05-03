from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.LoginPage, name = 'login'),
    path('logout/', views.LogoutUser, name = 'logout'),
    path('register/', views.registerPage, name = 'register'),


    path('profile/', include('Profile.urls')),
]
