from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.landing, name='landing'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('profile/<str:pk>/', views.profile, name='profile'),
    path('editprofile/<str:pk>/', views.editprofile, name='editprofile'),
    path('forum/', views.forum, name='forum'),
    path('listings/', views.listings, name='listings'),

]
