from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from Profile.models import ProfileData, ProfileLikes
from .models import Chat, Message

# Create your views here.
@login_required(login_url='/login/')
def home(request):

    current_userid = request.user.id
    current_profile = ProfileData.objects.get(user_id=current_userid)
    #все запросы на добавление в друзья
    couple_requests = current_profile.profilelikes_set.filter(like_id=current_profile.user_id)

    couples = []
    for couple in couple_requests:
        temp = ProfileData.objects.get(user_id=couple.likerid)
        couples.append(temp)


    if couples:
        current_couple = couples[0]
    else: current_couple = None

    if request.method == 'POST':
        if request.POST.get('like') == 'like':
            chat = Chat.objects.create(member_one=current_profile, member_two=current_couple)
            couple_requests[0].delete() #удаляем текущий запрос в друзья из БД
            couples.pop(0)
            if couples:
                current_couple = couples[0]
            else: current_couple = None
        elif request.POST.get('dislike') == 'dislike':
            couple_requests[0].delete() #удаляем текущий запрос в друзья из БД
            couples.pop(0)
            if couples:
                current_couple = couples[0]
            else: current_couple = None
        else:
            pass

    all_chats =  Chat.objects.all()
    contex = {
        'couple_request':current_couple,
        'all_chats':all_chats
    }

    return render(request, 'Chat/home.html', contex)