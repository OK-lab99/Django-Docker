from rest_framework import serializers
from blog.models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment','image')

        labels = {
            'comment':'コメント',
            'image':'写真',
        }

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        
        fields = (
            'text',
            'tags',
            'image',
        )