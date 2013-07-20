from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=60) # Field name made lowercase.
    class Meta:
        db_table = u'Category'
    
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    category = models.ForeignKey(Category, null=True)
    institution = models.CharField(max_length=30L, null=True)
    phone = models.CharField(max_length=30L, null=True)
    description = models.TextField(blank=True)
    
    class Meta:
        db_table = u'UserProfile'
    
    def __unicode__(self):
        return self.user.get_full_name()
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
