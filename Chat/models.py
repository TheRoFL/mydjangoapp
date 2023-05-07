from django.db import models
from Profile.models import ProfileData, ProfileLikes

class Chat(models.Model):
    member_one = models.ForeignKey(ProfileData, on_delete = models.CASCADE, blank=False, null=False, related_name = 'member_one')
    member_two = models.ForeignKey(ProfileData, on_delete = models.CASCADE, blank=False, null=False, related_name = 'member_two')
    chat_avatar = models.ImageField(upload_to='chats/avatars', blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.member_one.user.username + ', ' + self.member_two.user.username




class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete = models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(ProfileData, on_delete = models.CASCADE, blank=True, null=True)
    message = models.CharField(max_length=500, blank=False, null=False)
    uploaded_image = models.FileField(upload_to='chats/message_pictures', blank=True, null=True)
    sent_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        if len(self.message) > 20: return self.message[:20] + '...'
        else: return self.message

