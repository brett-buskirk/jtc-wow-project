from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CreateUserForm, PostForm, EditProfileForm
from .models import *


# Create your views here.
def landing(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'landing.html')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'login.html', context)


@login_required(login_url='landing')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='landing')
def editprofile(request):
    user = request.user.profile
    form = EditProfileForm(instance=user)
    context = {'form': form}
    return render(request, 'editprofile.html', context)


@login_required(login_url='landing')
def forum(request):
    if request.method == 'GET':
        form = PostForm()
        posts = Post.objects.all().order_by('-date_created')
        page = request.GET.get('page', 1)
        paginator = Paginator(posts, 2)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context = {'form': form, 'posts': posts}
        return render(request, 'forum.html', context)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            if 'create' in request.POST:
                post = form.cleaned_data.get('post')
                tags = form.cleaned_data.get('tags')
                forum_post = Post(post=post, user_id=request.user)
                forum_post.save()
                forum_post.tags.set(tags)
    return HttpResponseRedirect(reverse('forum'))


@login_required(login_url='landing')
def listings(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'listings.html', context)


def logoutUser(request):
    logout(request)
    return redirect('landing')


@login_required(login_url='landing')
def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)
