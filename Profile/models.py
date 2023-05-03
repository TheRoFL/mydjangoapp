from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.utils import IntegrityError
from django.core.validators import int_list_validator


# Create your models here.
class ProfileData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20,blank=False, null=False)
    surname = models.CharField(max_length=20, blank=False, null=False)
    birthdate = models.DateField(blank=False, null=False)

    SEX_CHOICES = (
            ('m', 'Male'),
            ('f', 'Female'),
        )

    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=False, null=False)
    preferences = models.CharField(max_length=1, choices=SEX_CHOICES, blank=False, null=False)
    interests = models.TextField(validators=[int_list_validator], max_length=100)
    sexualorientation = models.TextField(validators=[int_list_validator], max_length=100)

    avatar = models.ImageField(upload_to='avatars')
  
    acquaintances_available = models.IntegerField(default=0, blank=True, null=True)
    current_acquaintance = models.IntegerField(default=0, blank=True, null=True)
    
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        try:
            super(ProfileData, self).save(*args, **kwargs)
        except IntegrityError:
            raise ValueError('Такой email уже занят. Пожалуйста, введите другой email.')



class ProfileLikes(models.Model):
    like = models.ForeignKey(ProfileData, on_delete = models.CASCADE, blank=True, null=True)
    likerid = models.IntegerField(blank=True, null=True)
    message = models.CharField(max_length=255, default="", blank=True, null=True)

    def __str__(self):
        return ProfileData.objects.get(user_id=self.like).user.username