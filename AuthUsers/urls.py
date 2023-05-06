from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('Signup/', views.user_signup, name='user_signup'),
    path('logout/', views.user_logout, name='user_logout'),
    path('changepass/', views.changepass1, name='user_change_pass'),
    path('Uprofile/', views.user_profile, name='user_profile'),
    path('userdetail/<int:pk>/', views.User_details, name='user_detail'),
]
