from typing import Tuple
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from cloudinary.models import CloudinaryField
'''
CATEGORY = (('国語', '国語'),
        ('数学', '数学'),
        ('英語', '英語'),
        ('理科', '理科'),
        ('社会', '社会'),
        ('その他', 'その他'),
    )
'''
class Tag(models.Model):
    CATEGORY = (
        ('1', '国語'),
        ('2', '数学'),
        ('3', '英語'),
        ('4', '理科'),
        ('5', '社会'),
        ('6', 'その他'),
    )
    name = models.CharField(max_length=10, choices=CATEGORY)
    
    def __str__(self):
        return self.name 

class Article(models.Model):
    
    text = models.TextField(default='')
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    created_at = models.DateField(auto_now_add=True)
    
    updated_at = models.DateField(auto_now=True)
    
    count = models.IntegerField(default=0)
    
    tags = models.ManyToManyField(Tag, blank=True)

    image = models.ImageField(upload_to='media/problem', null=True, blank=True)

    able = models.BooleanField(default=False)

                                
class Comment(models.Model):
    comment = models.TextField(default='', max_length=500)
    
    created_at = models.DateField(auto_now_add=True)
     
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='media/answer', null=True, blank=True)

    
    
