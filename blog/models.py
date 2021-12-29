from typing import Tuple
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class Tag(models.Model):
    CATEGORY = (
        ('国語', '国語'),
        ('数学', '数学'),
        ('英語', '英語'),
        ('理科', '理科'),
        ('社会', '社会'),
        ('その他', 'その他'),
    )
    name = models.CharField(max_length=30, choices=CATEGORY)
    
    def __str__(self):
        return self.name 

class Article(models.Model):
    
    text = models.TextField(default='')
    
    author = models.CharField(default='',max_length=30)
    
    created_at = models.DateField(auto_now_add=True)
    
    updated_at = models.DateField(auto_now=True)
    
    count = models.IntegerField(default=0)
    
    tags = models.ManyToManyField(Tag, blank=True)

    image = models.ImageField(upload_to='problem', null=True, blank=True)
                                
class Comment(models.Model):
    comment = models.TextField(default='', max_length=500)
    
    created_at = models.DateField(auto_now_add=True)
     
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='answer', null=True, blank=True)

class Image(models.Model): 
    image = models.ImageField(verbose_name='問題', upload_to='images', null=True, blank=True)

    
    
