from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.landing, name='landing'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('profile/', views.profile, name='profile'),
    path('editprofile/', views.profile, name='editprofile'),
    path('forums/', views.profile, name='forums'),
    path('listings/', views.profile, name='listings'),

]
