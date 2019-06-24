from django.urls import path

from . import views

app_name = 'futeboladas'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('manage_profile/', views.manage_profile, name='manage_profile'),
    path('create_game/', views.create_game, name='create_game'),
    path('games/', views.GamesListView.as_view(), name='games'),
    path('games/<slug:game_id>/', views.game_detail, name='game_detail'),
    path('friends/', views.friends, name='friends'),
]