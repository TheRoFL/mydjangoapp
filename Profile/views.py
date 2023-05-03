from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ProfileData
from .forms import ProfileForm



@login_required(login_url='/login/')
def profile(request):
    form = ProfileForm()
    currentuserid = request.user.id
    try:
        currentuser = ProfileData.objects.get(user_id=currentuserid)
    except ProfileData.DoesNotExist:
        currentuser = None
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')

        else: return HttpResponse("Форма не валидна")

    context = {
        'currentuser': currentuser,
        'form': form
    }
    return render(request, 'Profile/profile.html', context)


def profile_editing(request):
    MyProfileData = get_object_or_404(ProfileData, pk = request.user.id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=MyProfileData)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')

        else: return HttpResponse("Форма не валидна")
    else:
         form = ProfileForm(instance=MyProfileData)

    context = {
        'form': form
    }
    return render(request, 'Profile/profile-editing.html', context)
