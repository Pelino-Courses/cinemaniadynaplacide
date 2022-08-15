from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('add-movie/', views.add_movie, name='add-movie'),
    path('movies/', views.movies_page, name='movies-list'),
    # path('/single-movie/<str:pk>', views.single_movie, name='single-movie'),
    path('profile/', views.user_profile, name='user-profile'),
    path('logout/', views.logoutUser, name='logout-user'),
]
