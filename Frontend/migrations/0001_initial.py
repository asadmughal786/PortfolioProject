# Generated by Django 4.2.1 on 2023-05-05 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('country', models.CharField(max_length=30, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('Name_of_degree', models.CharField(max_length=30, null=True)),
                ('user_education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='USER_ID')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('education_obj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalExperiance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('country', models.CharField(max_length=30, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('Company_name', models.CharField(max_length=30, null=True)),
                ('user_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User_id')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('prof_exp_obj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=30, null=True)),
                ('grip_value', models.SmallIntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User_id')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('Skill_obj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionlAchivements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achivements_name', models.CharField(max_length=30)),
                ('certification_link', models.URLField(null=True)),
                ('certification_start_date', models.DateField(null=True)),
                ('certification_end_date', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('p_achievement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Frontend.professionalexperiance', verbose_name='p_exp_id')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('p_achievements_obj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='EducativeAchivements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achivements_name', models.CharField(max_length=30)),
                ('certification_link', models.URLField(null=True)),
                ('certification_start_date', models.DateField(null=True)),
                ('certification_end_date', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Frontend.education', verbose_name='education_id')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('edu_achivements_obj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CompanySkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=30, null=True)),
                ('grip_value', models.SmallIntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('p_skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Frontend.professionalexperiance', verbose_name='Prof_exp_id')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('prof_skill_obj', django.db.models.manager.Manager()),
            ],
        ),
    ]
