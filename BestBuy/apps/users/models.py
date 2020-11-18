from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver




# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=True)
    first_name = models.CharField(max_length=100, null=True)
    

    def __str__(self): 
      return "{}".format(self.email) 


@receiver(post_save, sender=AbstractUser)
def create_profile(sender, instance, created, **kwargs):
        if created:
            CustomUser.objects.create(user=instance)
    
@receiver(post_save, sender=AbstractUser)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()





