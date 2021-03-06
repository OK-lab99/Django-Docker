from django.shortcuts import render, redirect
from account.models import Profile
from blog.models import Article
from django.contrib.auth.views import LoginView 
from account.forms import UserCreationForm, ProfileForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.mail import send_mail
import os

def index(request):
    ranks = Article.objects.order_by('-count')[:2]
    objs = Article.objects.all()
    context = {
        'articles' : objs, 
        'ranks' : ranks,
    }
    return render(request,'account/index.html', context)

class Login(LoginView):
    template_name = 'account/auth.html'
    
    def form_valid(self,form):
        messages.success(self.request, 'ログイン完了')
        return super().form_valid(form)
        
    def form_invalid(self,form):
        messages.error(self.request, 'エラーがあります')
        return super().form_invalid(form)
    
def signup(request):
    context = {}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            messages.success(request, '登録完了')
            return redirect('/')
    
    return render(request, 'account/auth.html', context)

@login_required
def mypage(request):
    context = {}
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, '更新完了しました')
            return redirect('/view_mypage/')
    else:
        form = ProfileForm()
    context['form'] = form
    return render(request, 'account/mypage.html', context)

@login_required
def view_mypage(request):
    profile = Profile.objects.all()
    articles = Article.objects.filter(user_id=request.user.pk)
    context = {
        'profile':profile,
        'articles':articles
    }
    
    return render(request, 'account/view.html', context)

def contact(request):
    context = {}
    if request.method == "POST":
        subject = 'お問い合わせがありました'
        message = """お問い合わせがありました。\n
        名前: {}\nメールアドレス: {}\n内容: {}""".format(
            request.POST.get('name'),
            request.POST.get('email'),
            request.POST.get('content'))
        email_from = os.environ['DEFAULT_EMAIL_FROM']
        email_to = [os.environ['DEFAULT_EMAIL_FROM'],]
        send_mail(subject, message, email_from, email_to)
        messages.success(request,'お問い合わせいただきありがとうございます。')
    return render(request, 'account/contact.html', context)

def explain(request):
    context = {}
    return render(request, 'account/explain.html', context)