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


# Landing Page
def landing(request):
    # If the user is already logged in, send them to the dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    # Otherwise, render the Landing Page
    else:
        return render(request, 'landing.html')


# Register Page
def registerPage(request):
    # If the user is already logged in, redirect them to the dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    # Otherwise either create a new user or render the Register Page
    else:
        # Create a user form instance
        form = CreateUserForm()
        # If a new user is created, save the user and create a new profile
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                new_user = User.objects.get(username=form.cleaned_data.get('username'))
                new_profile = Profile(user=new_user)
                new_profile.save()
                user = form.cleaned_data.get('username')
                
                # Notify the user of success and redirect to the Login Page
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
            
        # Otherwise render the Register Page
        context = {'form': form}
        return render(request, 'register.html', context)


# Login Page
def loginPage(request):
    # If a user is already logged in, redirect them to the Dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    # Otherwise render Login Page or attempt login
    else:
        # Login attempt
        if request.method == 'POST':
            # Gather username and password
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Attempt to authenticate the user
            user = authenticate(request, username=username, password=password)

            # If the user exists, log them in and redirect to Dashboard
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            
            # Otherwise display a message for incorrect login
            else:
                messages.info(request, 'Username or Password is incorrect')

        # Render the Login Page
        context = {}
        return render(request, 'login.html', context)


# Profile Page (Only logged in users can access this page)
@login_required(login_url='landing')
def profile(request, pk):
    # get user's profile from the database
    profile = Profile.objects.get(id=pk)
    # get all the posts for that user in the database newest first
    posts = Post.objects.all().order_by('-date_created').filter(user_id_id=profile.id)
    # set the number of posts per page to 5 in this instance
    paginate_posts = Paginator(posts, 5)
    # set the first page
    page = request.GET.get('page', 1)
    # set the page
    posts_page_obj = paginate_posts.get_page(page)
    # Create the context
    context = {
        "profile": profile, 
        "posts": posts_page_obj,
        "current_user": request.user.profile.id,
        "user_id": request.user.id
    }
    # Render the Profile Page
    return render(request, 'profile.html', context)


# Edit Profile Page (Only logged in users can access this page)
@login_required(login_url='landing')
def editprofile(request, pk):
    # Get the user's profile from the database
    profile = Profile.objects.get(user_id=pk)
    # Create an instance of the edit profile form
    form = EditProfileForm(instance=profile)
    
    # If an edit to a profile is made, check the form and make edits if valid
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    
    # Otherwise, render the Edit Profile Page
    context = {'form': form}
    return render(request, 'editprofile.html', context)


# Forum Page (Only logged in users can access this page)
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
        # Create the context
        context = {
            'form': form,
            'post_filter': post_filter, 
            'posts_page_obj': posts_page_obj,
            "current_user": request.user.profile.id
        }
        # Render the Forum Page
        return render(request, 'forum.html', context)

    # If a post is made on the Forum Page, verify data and create new post
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            if 'create' in request.POST:
                post = form.cleaned_data.get('post')
                tags = form.cleaned_data.get('tags')
                print(tags)
                forum_post = Post(post=post, user_id=request.user.profile)
                forum_post.save()
                for tag in tags:
                    forum_post.tags.add(tag)
                    
    # Redirect to the Forum Page
    return HttpResponseRedirect(reverse('forum'))


# Listings Page (Only logged in users can access this page)
@login_required(login_url='landing')
def listings(request):
    # Grab all the profiles in the database
    profiles = Profile.objects.all()
    # Create the context
    context = {
        'profiles': profiles,
        'current_user': request.user.profile.id
    }
    # Render the Listings Page
    return render(request, 'listings.html', context)


# Logout User Handler
def logoutUser(request):
    # Log out the current user
    logout(request)
    # Redirect to the Landing Page
    return redirect('landing')


# Dashboard Page (Only logged in users can access this page)
@login_required(login_url='landing')
def dashboard(request):
    context = {}
    # Render the Dashboard Page
    return render(request, 'dashboard.html', context)


# Delete Post Handler (Only logged in users can access this handler)
@login_required(login_url='landing')
def delete_post(request):
    # Delete request made in submit element (which is why it's POST vs. DELETE)
    if request.method == 'POST':
        # Grab the id of the post
        post_id = request.POST.get('post_id', None)
        # Delete the post
        Post.objects.get(post_id=post_id).delete()
        # Redirect back to the Profile Page
        return HttpResponseRedirect(reverse("profile", kwargs={'pk': request.user.profile.id}))
