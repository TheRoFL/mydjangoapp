from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Profile.models import ProfileData, ProfileLikes



@login_required(login_url='/login/')
def home(request):
    #считываем текущую анкету
    current_userid = request.user.id
    current_profile = ProfileData.objects.get(user_id=current_userid)

    #определяем пол для поиска анкет
    if current_profile.preferences == 'm':
        sex = 'm'
    else:
        sex = 'f'

    #все подходящие анкеты исходя из пола
    profiles = ProfileData.objects.filter(sex=sex)

    #подсчет и сохранение в БД количества доступных анкет
    current_profile.acquaintances_available = len(profiles)
    current_profile.save()

    #проверяем поле текущей анкеты, если = NULL, значит, зашел первый раз и необходимо присвоить ее 0
    if current_profile.current_acquaintance == None:
        current_profile.current_acquaintance = 0
        counter = 0
        current_profile.save()

    else: counter = current_profile.current_acquaintance


    current_profileToBeLiked = profiles[0]

    if request.method == 'GET':
        if counter < len(profiles):
            current_profileToBeLiked = profiles[counter]
        else:
            current_profileToBeLiked = None


    if request.method == 'POST':
        current_profileToBeLiked = profiles[counter]
        #проверяем, что мы не лайкнем уже лайкнутую анкету
        already_liked = current_profileToBeLiked.profilelikes_set.filter(like_id=current_profileToBeLiked).filter(likerid=request.user.id)

        print('already_liked = ', already_liked)
        if not already_liked:
            print(request.POST)
            if request.POST.get('like') == 'like':
                like1 = ProfileLikes.objects.create(like_id=current_profileToBeLiked.user_id, likerid=request.user.id)
            elif request.POST.get('dislike') == 'dislike':
                like1 = None
            else:
                like1 = ProfileLikes.objects.create(like_id=current_profileToBeLiked.user_id, likerid=request.user.id, message=request.POST.get('message'))
                print("current_profileToBeLiked:", current_profileToBeLiked.user_id)
                print("current_userid:", current_userid)

        counter = counter + 1
        current_profile.current_acquaintance = counter
        current_profile.save()

        if counter < len(profiles):
            current_profileToBeLiked = profiles[counter]

        else:
            current_profileToBeLiked = None



    contex = {'current_profileToBeLiked': current_profileToBeLiked}
    return render(request, 'Acquaintance/home.html', contex)