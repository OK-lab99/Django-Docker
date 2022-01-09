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
        CATEGORY = (
            ('国語', '国語'),
            ('数学', '数学'),
            ('英語', '英語'),
            ('理科', '理科'),
            ('社会', '社会'),
            ('その他', 'その他'),
        )   
        tags = forms.fields.ChoiceField(
            choices=CATEGORY,
            required=True,
        )
