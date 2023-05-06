from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('addskills/',views.add_skills,name='add_skills'),
]
