from django.db import models
from social_django.models import UserSocialAuth

# Create your models here.
class Message(models.Model):

    message = models.TextField(max_length=10000) #formでtext area
    user = models.ForeignKey(UserSocialAuth, on_delete=models.SET_NULL, null=True)
