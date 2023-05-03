from django.contrib import admin
from .models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class AuthUsers(admin.ModelAdmin):
    list_display = ['id','username','first_name','last_name','is_staff','email','user_phone','user_address','user_city','user_website']