from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.user_login,name='user_login'),
    path('reg/',views.user_signup,name='reg'),
]
