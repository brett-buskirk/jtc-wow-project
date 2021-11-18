from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm


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
      
    context = { 'form': form }
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


def logoutUser(request):
  logout(request)
  return redirect('landing')


@login_required(login_url='landing')
def dashboard(request):
  context = {}
  return render(request, 'dashboard.html', context)