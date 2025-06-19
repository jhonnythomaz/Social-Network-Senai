# Arquivo: rede_social/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomAuthenticationForm

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('post/create/', views.create_post_view, name='create_post'),
    path('post/<int:post_id>/', views.post_detail_view, name='post_detail'),
    path('post/<int:post_id>/like/', views.like_post_view, name='like_post'),
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path('users/', views.all_users_view, name='all_users'),
    path('invites/', views.invites_view, name='invites'),
    path('send-invite/<int:user_id>/', views.send_invite_view, name='send_invite'),
    path('accept-invite/<uuid:invite_id>/', views.accept_invite_view, name='accept_invite'),
    path('reject-invite/<uuid:invite_id>/', views.reject_invite_view, name='reject_invite'),
    path('notifications/', views.notification_view, name='notifications'),
    
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(
            template_name='pages/login.html',
            authentication_form=CustomAuthenticationForm
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]