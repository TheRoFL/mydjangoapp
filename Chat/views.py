from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import *
from Chat.models import Chat 
from django.shortcuts import get_object_or_404
from Profile.models import ProfileData, ProfileLikes

@login_required(login_url='/login/')
def home(request):

    current_userid = request.user.id
    try:
        current_profile = ProfileData.objects.get(user_id=current_userid)
    except ProfileData.DoesNotExist:
        return redirect('/profile')
    #все запросы на добавление в друзья
    couple_requests = current_profile.profilelikes_set.filter(like_id=current_profile.user_id)

    #создаем список пар, для добавления в друзья
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

    #Выбираем только те чаты, в которых мы состоим 
    all_chats =  Chat.objects.filter(Q(member_one=current_userid)
                                    |Q(member_two=current_userid))

    
    if current_couple:
        current_message = ProfileLikes.objects.get(likerid=current_couple.user_id)
    else: current_message = None

    
    contex = {
        'couple_request':current_couple,
        'all_chats':all_chats,
        'message':current_message,
    }

    return render(request, "chat/home.html", contex)


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    chat =  Chat.objects.filter(id=room_name)
    
    current_user = ProfileData.objects.get(user=request.user)
    contex = {
        "room_name": room_name,
        "chat": chat,
        'current_user':current_user
    }
    return render(request, "chat/room.html", contex)

def get_last_10_messages(chatId):
    chat = get_object_or_404(Chat, id=chatId)
    return chat.messages.order_by('-timestamp').all()


def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    return get_object_or_404(ProfileData, user=user)


def get_current_chat(chatId):
    return get_object_or_404(Chat, id=chatId)