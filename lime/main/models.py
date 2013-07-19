from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    university = models.CharField(max_length=30L, null=True)
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
