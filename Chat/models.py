from django.db import models
from Profile.models import ProfileData, ProfileLikes
from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    contact = models.ForeignKey(
        ProfileData, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    uploaded_image = models.FileField(upload_to='chats/message_pictures/%Y/%m/%d/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    

class Chat(models.Model):
    member_one = models.ForeignKey(ProfileData, on_delete = models.CASCADE, blank=False, null=False, related_name = 'member_one')
    member_two = models.ForeignKey(ProfileData, on_delete = models.CASCADE, blank=False, null=False, related_name = 'member_two')
    created_time = models.DateTimeField(auto_now_add=True)

    messages = models.ManyToManyField(Message, blank=True)
    
    def __str__(self):
        return self.member_one.user.username + ', ' + self.member_two.user.username
