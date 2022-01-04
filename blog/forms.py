from django import forms
from blog.models import Article, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment','image')

        labels = {
            'comment':'コメント',
            'image':'写真',
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        
        fields = (
            'text',
            'tags',
            'image',
        )