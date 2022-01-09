from django.shortcuts import render, redirect
from blog.models import Article, Comment, Tag
from django.core.paginator import Paginator
from blog.forms import CommentForm, PostForm
from django.contrib import messages

def index(request):
    objs = Article.objects.all()
    paginator = Paginator(objs,3)
    page_number = request.GET.get('page')
    context = {
        'page_title' : '問題一覧',
        'page_obj' : paginator.get_page(page_number),
        'page_number' : page_number,
    }
    return render(request,'blog/blog1.html', context)


def article(request, pk):
    obj = Article.objects.get(pk=pk)
    context = {}
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.article = obj
            answer.save()
            messages.success(request, '回答できました')
            return redirect('/blog/{}/'.format(pk))
        
        elif request.POST.get('like_count', None):
            obj.count += 1
            obj.save()
    
    else:
        form = CommentForm()
    comments = Comment.objects.filter(article=obj)
    context = {
        'article':obj,
        'comments':comments,
    }
    context['form'] = form
    return render(request,'blog/article.html', context)

def tags(request, name):
    tag = Tag.objects.get(name=name)
    objs = tag.article_set.all()
    
    paginator = Paginator(objs, 10)
    page_number = request.GET.get('page')
    context = {
        'page_title' : name,
        'page_obj' : paginator.get_page(page_number),
        'page_number' : page_number,
    }
    
    return render(request, 'blog/blog1.html', context)

def posts(request):
    context = {}
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            messages.success(request, '質問できました')
            return redirect('/')
    else:
        form = PostForm()
    context['form'] = form
   
    return render(request, 'blog/post.html', context)