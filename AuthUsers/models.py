from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth.models import AbstractUser
# Create your models here.

class BaseCreatedAtModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=30,blank=False,null=True)
    country = models.CharField(max_length=30,blank=False,null=True)
    class Meta:
        abstract = True

class BaseStartAtEndAt(models.Model):
    start_date = models.DateField(blank=False,null=True)
    end_date = models.DateField(blank=False,null=True)
    class Meta:
        abstract = True

class BaseAchivementsModel(models.Model):
    achivements_name = models.CharField(max_length=30)
    certification_link = models.URLField(null=True)
    certification_start_date = models.DateField(null=True)
    certification_end_date = models.DateField(null=True)
    class Meta:
        abstract = True

class BaseSkillsModel(models.Model):
    skill_name = models.CharField(max_length=30,null=True)
    grip_value = models.SmallIntegerField(blank=False,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False)
    class Meta:
        abstract = True

class CustomUser(AbstractUser):
    user_age = models.IntegerField(blank=False,null=True)
    user_city = models.CharField(max_length=30,blank=False,null=True)
    user_phone = PhoneNumberField(region='PK')
    user_address= models.TextField(blank=False,null=True)
    user_freelancer = models.BooleanField(blank=False,null=True)
    user_bio = models.TextField(max_length=255,blank=False,null=True)
    profile_picture = models.ImageField(upload_to='image/%y',blank=True,default=None)
    user_website = models.URLField(blank=False,null=False)

class Education(BaseStartAtEndAt,BaseCreatedAtModel):
    user_education = models.ForeignKey(CustomUser, verbose_name=("USER_ID"), on_delete=models.CASCADE)
    Name_of_degree = models.CharField(max_length=30,blank=False,null=True)
    education_obj = models.Manager()

class skills(BaseSkillsModel):
    user_skills = models.ForeignKey(CustomUser,verbose_name=('User_id'),on_delete=models.CASCADE)
    Skill_obj = models.Manager()

class professional_experiance(BaseStartAtEndAt,BaseCreatedAtModel):
    user_company = models.ForeignKey(CustomUser,verbose_name=('User_id'),on_delete=models.CASCADE)
    Company_name = models.CharField(max_length=30 , blank=False,null=True)
    prof_exp_obj = models.Manager()

class Educative_achivements(BaseAchivementsModel):
    education = models.ForeignKey(Education, verbose_name=("education_id"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    edu_achivements_obj = models.Manager()

class professionl_achivements(BaseAchivementsModel):
    p_achievement = models.ForeignKey(professional_experiance,verbose_name=('p_exp_id'), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    p_achievements_obj = models.Manager()

class Company_skills(BaseSkillsModel):
    p_skills = models.ForeignKey(professional_experiance,verbose_name=('Prof_exp_id'),on_delete=models.CASCADE)
    prof_skill_obj = models.Manager()