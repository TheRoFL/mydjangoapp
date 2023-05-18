from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from Profile.models import ProfileData, ProfileLikes
from .models import Chat, Message

# Create your views here.
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
        'message':current_message
    }

    return render(request, 'Chat/home.html', contex)

def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

def chat(request, pk):

    current_userid = request.user.id
    current_profile = ProfileData.objects.get(user_id=current_userid)

    has_access = Chat.objects.filter(Q(member_one=current_userid) | Q(member_two=current_userid))
    if has_access:
        current_chat = Chat.objects.get(id=pk)
    else: 
        current_chat = None
        return HttpResponse("Error 404")

    all_messages = Message.objects.filter(chat_id=current_chat)
    if request.method == 'POST':
        mes = request.POST.get('message')
        message = Message.objects.create(chat=current_chat, message=mes)
        message.author_id = current_userid
        message.save()


    contex = {
        'pk': pk, 
        'current_chat': current_chat,
        'all_messages': all_messages,
        'current_profile': current_profile
    }
    return render(request, 'Chat/chat.html', contex)