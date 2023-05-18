from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chats/<str:pk>/', views.chat),
    path('test/', views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
]