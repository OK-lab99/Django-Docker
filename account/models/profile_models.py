from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth import get_user_model

class Profile(models.Model):
    user = OneToOneField(get_user_model(), unique=True, on_delete=models.CASCADE, primary_key=True)
    
    username = models.CharField(default="匿名ユーザー", max_length=30)

    image = models.ImageField(upload_to='media/account', null=True, blank=True)

    age = models.PositiveSmallIntegerField(blank=True, null=True, default=0)

    text = models.TextField(default="")