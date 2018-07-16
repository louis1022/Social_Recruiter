from django.db import models
from social_django.models import UserSocialAuth

# Create your models here.
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    screen_name = models.CharField(max_length=128)
    follower_count = models.IntegerField()
    follow_count = models.IntegerField()
    descriptionn = models.TextField()

class Message(models.Model):

    message = models.TextField(max_length=10000) #formでtext area
    user = models.ForeignKey(UserSocialAuth, on_delete=models.SET_NULL, null=True)

