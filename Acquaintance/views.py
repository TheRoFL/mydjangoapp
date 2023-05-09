from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import date
from Profile.models import ProfileData, ProfileLikes
from Chat.models import Chat

from .models import Filter


@login_required(login_url='/login/')
def home(request):
    #считываем текущую анкету
    current_userid = request.user.id
    try:
        current_profile = ProfileData.objects.get(user_id=current_userid)
    except ProfileData.DoesNotExist:
        return redirect('/profile')

    #определяем пол для поиска анкет
    if current_profile.preferences == 'm':
        sex = 'm'
    else:
        sex = 'f'

    #все подходящие анкеты исходя из пола
    try:
        filt = Filter.objects.get(profile_data_id=current_profile.user.id)
    except Filter.DoesNotExist:
        filt = Filter(profile_data_id=current_profile.user.id)
        filt.save()
    #lte - lover the - т.е. ищет записи где рост больше filt.height_limit_lower
    profiles = ProfileData.objects.filter(
          Q(sex=sex) 
        & Q(personal_data__height__gte=filt.height_limit_lower) 
        & Q(personal_data__height__lte=filt.height_limit_upper)
        & Q(age__gte = filt.age_limit_lower) 
        & Q(age__lte = filt.age_limit_upper)
        )

    #подсчет и сохранение в БД количества доступных анкет
    current_profile.acquaintances_available = len(profiles)
    current_profile.save()

    #проверяем поле текущей анкеты, если = NULL, значит, зашел первый раз и необходимо присвоить ее 0
    if current_profile.current_acquaintance == None:
        current_profile.current_acquaintance = 0
        counter = 0
        current_profile.save()

    else: counter = current_profile.current_acquaintance


    if profiles:
        current_profileToBeLiked = profiles[0]
    else: current_profileToBeLiked = None

    if request.method == 'GET':
        if counter < len(profiles):
            if profiles:
                current_profileToBeLiked = profiles[counter]
            else: current_profileToBeLiked = None
        else:
            counter = 0
            current_profile.current_acquaintance = counter
            current_profile.save()
            if profiles:
                current_profileToBeLiked = profiles[0]
            else: current_profileToBeLiked = None


    if request.method == 'POST':
        current_profileToBeLiked = profiles[counter]
        #проверяем, что мы не лайкнем уже лайкнутую анкету
        already_liked = current_profileToBeLiked.profilelikes_set.filter(like_id=current_profileToBeLiked).filter(likerid=request.user.id)
        already_coupled = Chat.objects.filter(Q(member_one=current_profileToBeLiked.user.id, member_two=current_userid)
                                             |Q(member_one=current_userid, member_two=current_profileToBeLiked.user.id))

                                    
        if not already_liked and not already_coupled:
            if request.POST.get('like') == 'like':
                like1 = ProfileLikes.objects.create(like_id=current_profileToBeLiked.user_id, likerid=request.user.id)
            elif request.POST.get('dislike') == 'dislike':
                like1 = None
            elif request.POST.get('send') == 'send':
                like1 = ProfileLikes.objects.create(like_id=current_profileToBeLiked.user_id, likerid=request.user.id,
                message=request.POST.get('message'))
            else:
                pass

        counter += 1
        current_profile.current_acquaintance = counter
        current_profile.save()

        if counter < len(profiles):
            current_profileToBeLiked = profiles[counter]

        else:
            counter = 0
            current_profile.current_acquaintance = counter
            current_profile.save()
            current_profileToBeLiked = profiles[0]

    if current_profileToBeLiked:
        birth = str(current_profileToBeLiked.birthdate)
        year, month, day = map(int, birth.split('-'))
        birthdate = date(year, month, day)
        today = date.today()
        Age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    else:
        Age = None
    contex = {
         'currentuser': current_profileToBeLiked, 
         'age':Age 
    }
    return render(request, 'Acquaintance/home.html', contex)


@login_required(login_url='/login/')
def filter(request):
    #считываем текущую анкету
    current_userid = request.user.id
    try:
        current_profile = ProfileData.objects.get(user_id=current_userid)
    except ProfileData.DoesNotExist:
        return redirect('/profile')


    try:
        filt = Filter.objects.get(profile_data_id=current_profile.user.id)
    except Filter.DoesNotExist:
        filt = None


    if request.method == 'POST':
        filt.age_limit_lower = request.POST.get('age_limit_lower')
        filt.age_limit_upper = request.POST.get('age_limit_upper')
        filt.height_limit_lower = request.POST.get('height_limit_lower')
        filt.height_limit_upper = request.POST.get('height_limit_upper')

        filt.save()
        return redirect('/acquaintances')

    
    contex = {
        'filter':filt,
    }

    return render(request, 'Acquaintance/filter.html', contex)