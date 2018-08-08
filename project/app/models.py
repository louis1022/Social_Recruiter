from django.db import models
from social_django.models import UserSocialAuth

# Create your models here.
class Person(models.Model):    
    user_id = models.BigIntegerField(primary_key=True)
    screen_name =  models.CharField(max_length=128)
    location =  models.CharField(max_length=128)
    url =  models.CharField(max_length=128, null=True)
    discription = models.TextField(null=True)
    friends_count = models.IntegerField()
    followers_count = models.IntegerField()
    listed_count = models.IntegerField(null=True)
    favourites_count = models.IntegerField(null=True)
    statuses_count = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)

class Message(models.Model):

    message = models.TextField(max_length=10000) #formでtext area
    user = models.ForeignKey(UserSocialAuth, on_delete=models.SET_NULL, null=True)

class Introduce(models.Model):

    user = models.OneToOneField(UserSocialAuth, on_delete=models.SET_NULL, null=True)
    company_name = models.CharField(max_length=64)
    recruiter = models.CharField(max_length=32)

