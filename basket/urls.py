from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('connect/', views.connect, name='connect'),
    path('register/', views.register, name='register'),
    path('register_post/', views.register_post, name='register_post'),
    path('players/', views.all_players, name='players'),
    path('player/<int:player_id>/', views.player_detail, name='player_detail'),
    path('team_detail/<int:team_id>/', views.team_detail, name='team_detail'),
    path('teams/', views.all_teams, name='teams'),
    path('matchs/', views.all_matchs, name='matchs')
]
