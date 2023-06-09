from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile-editing/', views.profile_editing, name='profile-editing'),
    path('<str:Login>/', views.profileReview),
]
