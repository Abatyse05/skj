from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teams/', views.team_list, name='team_list'),
    path('add-player/', views.add_player, name='add_player'),
    path('players/', views.player_list, name='player_list'),
    path('add-team/', views.add_team, name='add_team'),
    path('add-ligue/', views.add_ligue, name='add_ligue'),
    path('edit-player/<int:player_id>/', views.edit_player, name='edit_player'),
    path('player/<int:player_id>/', views.player_detail, name='player_detail'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    path('edit-team/<int:team_id>/', views.edit_team, name='edit_team'),
    path('ligues/', views.ligue_list, name='ligue_list'),
    path('ligue/<int:ligue_id>/', views.ligue_detail, name='ligue_detail'),
    path('history/', views.player_history_list, name='player_history_list'),
    path('add-history/', views.add_player_history, name='add_player_history'),
]