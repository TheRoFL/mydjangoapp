from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ProfileData, Interests, PersonalData
from .forms import ProfileForm, InterestsForm, PersonalDataForm


step = 0
step_edit = 0
@login_required(login_url='/login/')
def profile(request):
    Profile_form = ProfileForm()
    Interests_form = InterestsForm()
    PersonalData_form = PersonalDataForm()
    currentuserid = request.user.id
    try:
        currentuser = ProfileData.objects.get(user_id=currentuserid)
    except ProfileData.DoesNotExist:
        currentuser = None
    
    global step

    if request.method == 'POST':

        if step == 0:
            Profile_form = ProfileForm(request.POST, request.FILES)
            if Profile_form.is_valid():
                profile = Profile_form.save(commit=False)
                profile.user = request.user
                profile.save()

                step = step + 1
            else: return HttpResponse("Форма не валидна1")

        elif step == 1:
            PersonalData_form = PersonalDataForm(request.POST)
            if PersonalData_form.is_valid():
                profile = get_object_or_404(ProfileData, pk = request.user.id)
                presonal_data = PersonalData_form.save(commit=False)
                profile.personal_data = presonal_data
                presonal_data.save()
                profile.save()

                step = step + 1

            else: return HttpResponse("Форма не валидна2")

        elif step == 2:
            Interests_form = InterestsForm(request.POST)
            if Interests_form.is_valid():
                profile = get_object_or_404(ProfileData, pk = request.user.id)
                interests = Interests_form.save(commit=False)
                profile.interests = interests
                interests.save()
                profile.save()

                step = 0
                return redirect('profile')
               

            else: return HttpResponse("Форма не валидна3")
       
        
    context = {
        'currentuser': currentuser,
        'Profile_form': Profile_form,
        'Interests_form': Interests_form,
        'PersonalData_form':PersonalData_form,
        'step':step,
    }
    
    return render(request, 'Profile/profile.html', context)


def profile_editing(request):

    currentuserid = request.user.id
    try:
        currentuser = ProfileData.objects.get(user_id=currentuserid)
    except ProfileData.DoesNotExist:
        currentuser = None

    MyProfileData = get_object_or_404(ProfileData, pk = request.user.id)
    MyPersonalData = get_object_or_404(PersonalData, pk = currentuser.personal_data_id)
    MyInterests = get_object_or_404(Interests, pk = currentuser.interests_id)

    global step_edit

    form = None

    if request.method == 'POST':
        if step_edit == 0:
            form = ProfileForm(request.POST, request.FILES, instance=MyProfileData)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()

                step_edit += 1
            else: return HttpResponse("Форма не валидна 1")


        elif step_edit == 1:
            form = PersonalDataForm(request.POST, instance=MyPersonalData)
            if form.is_valid():
                presonal_data = form.save(commit=False)
                presonal_data.save()
                step_edit += 1
            else: return HttpResponse("Форма не валидна 2")


        elif step_edit == 2:
            form = InterestsForm(request.POST, instance=MyInterests)
            if form.is_valid():
                interests = form.save(commit=False)
                interests.save()
                step_edit = 0
                return redirect('/profile')
            else: return HttpResponse("Форма не валидна 3")


    if step_edit == 0:
        form = ProfileForm(instance=MyProfileData)
    elif step_edit == 1:
        form = PersonalDataForm(instance=MyPersonalData)
    elif step_edit == 2:
        form = InterestsForm(instance=MyInterests)


    context = {
        'form': form,
        'step_edit':step_edit
    }
    return render(request, 'Profile/profile-editing.html', context)
