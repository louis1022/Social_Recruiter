from django.db import models
from social_django.models import UserSocialAuth

class Introduce(models.Model):

    user = models.OneToOneField(UserSocialAuth, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=64)
    recruiter = models.CharField(max_length=32)

