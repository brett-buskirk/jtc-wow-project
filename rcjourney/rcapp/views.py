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
from .filters import PostFilter


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
                new_user = User.objects.get(
                    username=form.cleaned_data.get('username'))
                new_profile = Profile(user=new_user)
                new_profile.save()
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
def profile(request, pk):
    # get user's profile from the database
    profile = Profile.objects.get(id=pk)
    # get all the posts for that user in the database newest first
    posts = Post.objects.all().order_by(
        '-date_created').filter(user_id_id=profile.id)
    # set the number of posts per page to 5 in this instance
    paginate_posts = Paginator(posts, 5)
    # set the first page
    page = request.GET.get('page', 1)
    # set the page
    posts_page_obj = paginate_posts.get_page(page)
    context = {
      "profile": profile, 
      "posts": posts_page_obj,
      "current_user": request.user.profile.id,
      "user_id": request.user.id
    }
    return render(request, 'profile.html', context)


@login_required(login_url='landing')
def editprofile(request, pk):
    profile = Profile.objects.get(user_id=pk)
    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'editprofile.html', context)


@login_required(login_url='landing')
def forum(request):
    if request.method == 'GET':
        # create a new instance of the post form
        form = PostForm()
        # get all of the posts from the database ordered newest to oldest
        posts = Post.objects.all().order_by('-date_created')
        # if the posts are to filtered filter them
        post_filter = PostFilter(request.GET, queryset=posts)
        # set the posts to the filtered posts
        posts = post_filter.qs
        # set the number of posts per page to 5 in this instance
        paginate_posts = Paginator(posts, 5)
        # set the first page
        page = request.GET.get('page', 1)
        # set the page
        posts_page_obj = paginate_posts.get_page(page)

        context = {
          'form': form,
          'post_filter': post_filter, 
          'posts_page_obj': posts_page_obj,
          "current_user": request.user.profile.id
          }
        return render(request, 'forum.html', context)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            if 'create' in request.POST:
                post = form.cleaned_data.get('post')
                tags = form.cleaned_data.get('tags')
                forum_post = Post(
                    post=post, user_id=request.user.profile)
                forum_post.save()
                for tag in tags:
                    forum_post.tags.add(tag)
    return HttpResponseRedirect(reverse('forum'))


@login_required(login_url='landing')
def listings(request):
    profiles = Profile.objects.all()
    print(profiles[0].user.id)
    context = {
      'profiles': profiles,
      "current_user": request.user.profile.id
    }
    return render(request, 'listings.html', context)


def logoutUser(request):
    logout(request)
    return redirect('landing')


@login_required(login_url='landing')
def dashboard(request):
    print(request.user)
    context = {}
    return render(request, 'dashboard.html', context)


@login_required(login_url='landing')
def delete_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id', None)
        Post.objects.get(post_id=post_id).delete()
        return HttpResponseRedirect(reverse("profile", kwargs={'pk': request.user.profile.id}))
