from django.contrib.auth import get_user_model
from django.db import models
from Profile.models import ProfileData


User = get_user_model()

# class Chat(models.Model):
#     member_one = models.ForeignKey(ProfileData, on_delete = models.CASCADE, blank=False, null=False, related_name = 'member_one')
#     member_two = models.ForeignKey(ProfileData, on_delete = models.CASCADE, blank=False, null=False, related_name = 'member_two')
#     chat_avatar = models.ImageField(upload_to='chats/avatars/%Y/%m/%d/', blank=True, null=True)
#     created_time = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.member_one.user.username + ', ' + self.member_two.user.username




# class Message(models.Model):
#     chat = models.ForeignKey(Chat, on_delete = models.CASCADE, blank=True, null=True)
#     author = models.ForeignKey(ProfileData, on_delete = models.CASCADE, blank=True, null=True)
#     message = models.CharField(max_length=500, blank=False, null=False)
#     uploaded_image = models.FileField(upload_to='chats/message_pictures/%Y/%m/%d/', blank=True, null=True)
#     sent_time = models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         if len(self.message) > 20: return self.message[:20] + '...'
#         else: return self.message


class Contact(models.Model):
    user = models.ForeignKey(
        User, related_name='friends', on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    contact = models.ForeignKey(
        Contact, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact.user.username


class Chat(models.Model):
    participants = models.ManyToManyField(
        Contact, related_name='chats', blank=True)
    messages = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return "{}".format(self.pk)