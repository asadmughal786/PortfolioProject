from typing import Any
from django.db import models
from AuthUsers.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth.models import AbstractUser


class BaseCreatedAtModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=30, blank=False, null=True)
    country = models.CharField(max_length=30, blank=False, null=True)

    class Meta:
        abstract = True


class BaseStartAtEndAt(models.Model):
    start_date = models.DateField(blank=False, null=True)
    end_date = models.DateField(blank=False, null=True)

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
    skill_name = models.CharField(max_length=30, null=True)
    grip_value = models.SmallIntegerField(blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Education(BaseStartAtEndAt, BaseCreatedAtModel):
    user_education = models.ForeignKey(
        CustomUser, verbose_name=("USER_ID"), on_delete=models.CASCADE)
    Name_of_degree = models.CharField(max_length=30, blank=False, null=True)
    education_obj = models.Manager()


class Skills(BaseSkillsModel):
    user_skills = models.ForeignKey(
        CustomUser, verbose_name=('User_id'), on_delete=models.CASCADE)
    Skill_obj = models.Manager()


class ProfessionalExperiance(BaseStartAtEndAt, BaseCreatedAtModel):
    user_company = models.ForeignKey(
        CustomUser, verbose_name=('User_id'), on_delete=models.CASCADE)
    Company_name = models.CharField(max_length=30, blank=False, null=True)
    prof_exp_obj = models.Manager()



class EducativeAchivements(BaseAchivementsModel):
    education = models.ForeignKey(Education, verbose_name=(
        "education_id"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    edu_achivements_obj = models.Manager()


class ProfessionlAchivements(BaseAchivementsModel):
    p_achievement = models.ForeignKey(
        ProfessionalExperiance, verbose_name=('p_exp_id'), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    p_achievements_obj = models.Manager()


class CompanySkills(BaseSkillsModel):
    p_skills = models.ForeignKey(ProfessionalExperiance, verbose_name=(
        'Prof_exp_id'), on_delete=models.CASCADE)
    prof_skill_obj = models.Manager()
