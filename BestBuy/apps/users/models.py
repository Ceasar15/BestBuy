from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
      username =None
      email = models.EmailField(_('email address'), max_length=100, null=True, unique=True)
      phone = models.CharField(max_length=15, null=True)
      first_name = models.CharField(max_length=100, null=True)
      last_name = models.CharField(max_length=100, null=True)
      last_login = models.DateTimeField(auto_now_add=True, null=True)    

      USERNAME_FIELD = 'email'
      REQUIRED_FIELDS = []

      objects = CustomUserManager()
      
      def __str__(self): 
        return "{}".format(self.email)             












# class CustomUser(AbstractUser):
#     email = models.EmailField(max_length=50, null=True)
#     phone = models.CharField(max_length=15, null=True)
#     first_name = models.CharField(max_length=100, null=True)
#     last_name = models.CharField(max_length=100, null=True)
#     last_login = models.DateTimeField(auto_now_add=True, null=True)    
    

#     def __str__(self): 
#       return "{}".format(self.email) 


# @receiver(post_save, sender=AbstractUser)
# def create_profile(sender, instance, created, **kwargs):
#         if created:
#             CustomUser.objects.create(user=instance)
    
# @receiver(post_save, sender=AbstractUser)
# def save_profile(sender, instance, **kwargs):
#         instance.profile.save()





