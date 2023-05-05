from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.utils import IntegrityError
from django.core.validators import int_list_validator



class Interests(models.Model):

    music = models.BooleanField(blank=True, null=True)
    travelling = models.BooleanField(blank=True, null=True)
    fashion = models.BooleanField(blank=True, null=True)
    hiking = models.BooleanField(blank=True, null=True)
    photographing = models.BooleanField(blank=True, null=True)
    parties_clubs= models.BooleanField(blank=True, null=True)
    art = models.BooleanField(blank=True, null=True)
    meditation = models.BooleanField(blank=True, null=True)
    football = models.BooleanField(blank=True, null=True)
    fishing_hunting = models.BooleanField(blank=True, null=True)
    running = models.BooleanField(blank=True, null=True)
    swimming = models.BooleanField(blank=True, null=True)
    cooking = models.BooleanField(blank=True, null=True)
    shoping = models.BooleanField(blank=True, null=True)
    restaurants = models.BooleanField(blank=True, null=True)
    cinema = models.BooleanField(blank=True, null=True)
    board_games= models.BooleanField(blank=True, null=True)
    blogging = models.BooleanField(blank=True, null=True)
    it = models.BooleanField(blank=True, null=True)
    dancing = models.BooleanField(blank=True, null=True)
    sport = models.BooleanField(blank=True, null=True)
    creativity = models.BooleanField(blank=True, null=True)
    books = models.BooleanField(blank=True, null=True)
     

class PersonalData(models.Model):

    STAT_CHOICES =(
                ('Не в отношениях', 'Не в отношениях'),
                ('В отношениях', 'В отношениях'),
                ('Все сложно', 'Все сложно'),
        )
    status = models.CharField(max_length=100, choices=STAT_CHOICES, blank=True, null=True)

    PURP_CHOICES = (
                ('Серьзные отношения', 'Серьзные отношения'),
                ('Свободные отношения', 'Свободные отношения'),
                ('Для развлечений', 'Для развлечений'),
                ('Временные', 'Временные'),
                ('Постоянные', 'Постоянные'),
                ('Отношения', 'Отношения'),
            )
    purpose = models.CharField(max_length=100, choices=PURP_CHOICES, blank=True, null=True)

    height = models.IntegerField(blank=True, null=True)
    
    DRINK_CHOICES = (
                ('Иногда', 'Иногда'),
                ('Редко', 'Редко'),
                ('Никогда', 'Никогда'),
    )
    drinking = models.CharField(max_length=100, choices=DRINK_CHOICES, blank=True, null=True)

    SMOKE_CHOICES = (
                ('Курю', 'Курю'),
                ('Редко курю', 'Редко курю'),
                ('Парю', 'Парю'),
                ('Не курю и не парю', 'Не курю и не парю'),
    )
    smoking = models.CharField(max_length=100, choices=SMOKE_CHOICES, blank=True, null=True)

    SPORT_CHOICES = (
                ('Постоянно', 'Постоянно'),
                ('Иногда', 'Иногда'),
                ('Редко', 'Редко'),
                ('Никогда', 'Никогда'),
    )
    sport = models.CharField(max_length=100, choices=SPORT_CHOICES, blank=True, null=True)

    CHILD_CHOICES = (
                ('Уже есть', 'Уже есть'),
                ('Нет, но хочу', 'Нет, но хочу'),
                ('Нет', 'Нет'),
                ('Чайлдфри', 'Чайлдфри'),
    )
    children = models.CharField(max_length=100, choices=CHILD_CHOICES, blank=True, null=True)


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
    about_you = models.CharField(max_length=255, blank=True, null=True)
    sexualorientation = models.TextField(validators=[int_list_validator], max_length=100)

  
    personal_data = models.OneToOneField(PersonalData, on_delete=models.CASCADE, blank=True, null=True)
    interests = models.OneToOneField(Interests, on_delete=models.CASCADE, blank=True, null=True)

    avatar = models.ImageField(upload_to='avatars')
  
    acquaintances_available = models.IntegerField(default=0, blank=True, null=True)
    current_acquaintance = models.IntegerField(default=0, blank=True, null=True)

    couples_requests = models.IntegerField(default=0, blank=True, null=True)

    
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
        return ProfileData.objects.get(user_id=self.likerid).user.username

    
