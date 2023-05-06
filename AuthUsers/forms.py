from .models import *
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from phonenumber_field.formfields import PhoneNumberField
from django import forms
from django.core import validators


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_city = forms.CharField(max_length=30, required=True)
    user_age = forms.IntegerField(
        validators=[validators.MaxValueValidator(100)])
    user_address = forms.CharField(widget=forms.Textarea(), validators=[
                                   validators.MaxLengthValidator(255)])
    user_freelancer = forms.BooleanField()
    user_phone = PhoneNumberField(region="PK", widget=PhoneNumberPrefixWidget(
        country_choices=[("PK", "Pakistan")]))
    user_bio = forms.CharField(widget=forms.Textarea(), validators=[
                               validators.MaxLengthValidator(255)])
    profile_picture = forms.ImageField(allow_empty_file=False, required=True)
    user_website = forms.URLInput()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(
        label="Confirm Password(again)", widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['profile_picture', 'username', 'email', 'first_name', 'last_name', 'password1', 'password2',
                  'user_age', 'user_phone', 'user_city', 'user_address', 'user_freelancer', 'user_bio', 'user_website']
        labels = {'username': 'Username', 'first_name': 'First Name',
                  'last_name': 'Last Name', 'email': 'Email Address'}


class EditUserProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name',
                  'email', 'date_joined', 'last_login']
        labels = {'email': 'Email'}


class EditAdminProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = '__all__'
        labels = {'email': 'Email'}
