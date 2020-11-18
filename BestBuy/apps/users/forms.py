from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.conf import settings

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
 

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'phone', 'first_name', 'last_name')    

    # def clean_email(self):
    #     email = self.cleaned_data['email'].lower()
    #     results = CustomUser.objects.filter(email=email)
    #     if results.count():
    #         raise ValidationError("Email already existsssssssss")
    #     return email

    # def save(self, commit= False):
    #     user = super().save(commit=False)
    #     user = CustomUser.objects.create_user(
    #         self.cleaned_data['email'],
    #         phone = self.cleaned_data['phone'],
    #         first_name = self.cleaned_data['first_name'],
    #         last_name = self.cleaned_data['last_name'],
    #         password = self.cleaned_data['password1'],
    #     )

        
        #return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'phone', 'first_name', 'last_name')


