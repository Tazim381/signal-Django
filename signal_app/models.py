from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    occupation = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.user.username}'s profile"

