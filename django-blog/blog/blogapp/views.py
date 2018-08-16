from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Post, Comment
from . import forms


def index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blogapp/index.html', context)


def detail(request, title):
    post = Post.objects.get(title=title)
    if request.method == 'POST':
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.post = post
            instance.user = request.user
            instance.save()
            return redirect('blog:detail', title)
    else:
        comments = Comment.objects.filter(post=post).order_by('-timestamp')
        form = forms.CreateComment()
        context = {'post': post, 'comments': comments, 'form': form}
        return render(request, 'blogapp/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(reverse('blog:index'))
    else:
        form = forms.CreatePost()
        return render(request, 'blogapp/create.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('blog:index'))
    else:
        form = UserCreationForm()
        return render(request, 'blogapp/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect(reverse('blog:index'))
    else:
        form = AuthenticationForm()
        return render(request, 'blogapp/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('blog:login'))
