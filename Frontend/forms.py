from .models import *
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from phonenumber_field.formfields import PhoneNumberField
from django import forms
from django.core import validators

class Education(forms.ModelForm):
    degree_name= forms.CharField(label="Degree Name",widget=forms.TextInput(attrs={'autocomplete':'off'}),validators=[validators.MaxLengthValidator(30)],required=True)
    degree_city = forms.CharField(label='City',widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'City'}),validators=[validators.MaxLengthValidator(15)])
    degree_country = forms.CharField(label='Country',widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'City'}),validators=[validators.MaxLengthValidator(15)])
    degree_start_date = forms.DateField(label="Degree Start Date",widget=forms.DateInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'Start Date'}))
    degree_end_date = forms.DateField(label="Degree End Date",widget=forms.DateInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'End Date'}))
    class Meta:
        model = Education
        fields =['degree_name','degree_city','degree_country','degree_start_date','degree_end_date']

class ProfessionalExp(forms.ModelForm):
    company_name = forms.CharField(label='Company Name', widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'Achievement title'}),validators=[validators.MaxLengthValidator(30)],required=True)
    company_city = forms.CharField(label='City',widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'City'}),validators=[validators.MaxLengthValidator(15)])
    company_country = forms.CharField(label='Country',widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'City'}),validators=[validators.MaxLengthValidator(15)])
    job_start_date = forms.DateField(label='Joining Date',widget=forms.DateInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'Start Date'}))
    job_end_date = forms.DateField(label='Ending Date',widget=forms.DateInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'End Date'}))
    class Meta:
        model = ProfessionalExperiance
        fields = ['company_name','company_city','company_country','job_start_date','job_end_date']

class Achivements(forms.ModelForm):
    achievement_title = forms.CharField(label='Achivement Title', widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'Achievement title'}),validators=[validators.MaxLengthValidator(30)],required=True)
    achievement_link = forms.URLField(label='Achivement URL',widget=forms.URLInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'https://www.google.com'}),validators=[validators.URLValidator()],required=True)
    certification_start_date = forms.DateField(label='Certification Start Date',widget=forms.DateInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'Start Date'}))
    certification_start_date = forms.DateField(label='Certification End Date',widget=forms.DateInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'End Date'}))
    class Meta:
        model = EducativeAchivements
        fields = ['achievement_title','achievement_link','certification_start_date','certification_start_date']

class SkillsForm(forms.ModelForm):
    skill_name = forms.CharField(label='Skill Name',widget=forms.TextInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'Skill Name'}),validators=[validators.MaxLengthValidator(30)],required=True)
    skill_grip_value = forms.IntegerField(label="How Much do you have Grip in this?",widget=forms.NumberInput(attrs={'autocomplete':'off','class':'form-control','placeholder':'Enter Value'}),validators=[validators.MaxValueValidator(100)],required=True)
    class Meta:
        model = Skills
        fields = ['skill_name','skill_grip_value']

class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields =['username','first_name','last_name','email','date_joined','last_login']
        labels = {'email':'Email'}


class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields ='__all__'
        labels = {'email':'Email'}