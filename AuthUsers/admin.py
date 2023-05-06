# from django.contrib import admin
# from django.contrib.auth.models import Group
# from .models import *

# # Register your models here.

# admin.site.unregister(Group)
# admin.site.site_header = 'My Django Portfolio Project'
# admin.site.site_title = 'Portfolio Admin Panel'
# admin.site.index_title = 'Portfolio Admin Panel'


# @admin.register(CustomUser)
# class AuthUsers(admin.ModelAdmin):
#     list_display = ['id', 'username', 'first_name', 'last_name', 'is_staff',
#                     'email', 'user_phone', 'user_address', 'user_city', 'user_website']
#     search_fields=['username','first_name','last_name','email']

#     def avatar_tag(self, obj):
#         return format_html('<img src="{}" width="50" height="50" />'.format(obj.profile_picture.url))

#     avatar_tag.short_description = 'Avatar'

# from django.contrib import admin
# from django.utils.html import format_html
# from .models import CustomUser

# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'avatar_tag', 'user_age', 'user_city', 'user_phone', 'user_address', 'user_freelancer', 'user_bio', 'user_website')
#     search_fields = ('username', 'email', 'user_city')
#     list_filter = ('user_city', 'user_freelancer')

#     def avatar_tag(self, obj):
#         return format_html('<img src="{}" width="50px" height="50px"/>'.format(obj.profile_picture.url))
#     avatar_tag.short_description = 'Avatar'

# admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser
from django.utils.html import format_html

admin.site.unregister(Group)
admin.site.site_header = 'My Django Portfolio Project'
admin.site.site_title = 'Portfolio Admin Panel'
admin.site.index_title = 'Portfolio Admin Panel'

class UserAdmin(BaseUserAdmin):

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'avatar_tag')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('avatar_tag','first_name', 'last_name', 'email', 'user_age', 'user_city', 'user_phone', 'user_address', 'user_freelancer', 'user_bio', 'profile_picture', 'user_website')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ['avatar_tag']

    def avatar_tag(self, obj):
        return format_html('<img src="{}" align = "middle" width="100px" height="100px"/>'.format(obj.profile_picture.url))
    avatar_tag.short_description = 'Avatar'

admin.site.register(CustomUser, UserAdmin)




