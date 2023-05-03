from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



def home(request):
    return render(request, 'base/home.html')


def LoginPage(request):
    page = 'login'
   
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Invalid username or password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
             messages.error(request, 'Incorrect password')

    contex = {'page' : page}
    return render(request, 'base/login_register.html', contex)


def LogoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            username = user.username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Login already exists')
            else:
                user.save()
                login(request, user)
                return redirect('home')     

    else:
        form = UserCreationForm()

    contex = {'form' : form}
    return render(request, 'base/login_register.html', contex)





