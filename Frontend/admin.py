from django.contrib import admin
from .models import Education,EducativeAchivements,ProfessionalExperiance,ProfessionlAchivements,Skills,CompanySkills

# Register your models here.


@admin.register(Education)
class UserEducation(admin.ModelAdmin):
    list_display = ['id', 'Name_of_degree', 'city', 'country', 'start_date',
                    'end_date', 'created_at', 'updated_at', 'user_education']


@admin.register(ProfessionalExperiance)
class UserProfessionalExp(admin.ModelAdmin):
    list_display = ['id', 'Company_name', 'start_date',
                    'end_date', 'created_at', 'updated_at', 'user_company']


@admin.register(Skills)
class Skills(admin.ModelAdmin):
    list_display = ['id', 'skill_name', 'grip_value',
                    'created_at', 'updated_at', 'user_skills']


@admin.register(EducativeAchivements)
class Educative_achivement(admin.ModelAdmin):
    list_display = ['id', 'achivements_name', 'certification_link', 'certification_start_date',
                    'certification_end_date', 'created_at', 'updated_at', 'education']


@admin.register(ProfessionlAchivements)
class professional_ahcivement(admin.ModelAdmin):
    list_display = ['id', 'achivements_name', 'certification_link', 'certification_start_date',
                    'certification_end_date', 'created_at', 'updated_at', 'p_achievement']


@admin.register(CompanySkills)
class comp_skills(admin.ModelAdmin):
    list_display = ['id', 'skill_name', 'created_at', 'updated_at', 'p_skills']
