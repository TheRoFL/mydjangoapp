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
                ('1', 'single'),
                ('2', 'in-relations'),
                ('3', 'complicated'),
        )
    status = models.CharField(max_length=1, choices=STAT_CHOICES, blank=True, null=True)

    PURP_CHOICES = (
                ('1', 'serious'),
                ('2', 'non-serious'),
                ('3', 'just-for-fun'),
                ('4', 'short-period'),
                ('5', 'long-period'),
                ('6', 'acquintances'),
            )
    purpose = models.CharField(max_length=1, choices=PURP_CHOICES, blank=True, null=True)

    height = models.IntegerField(blank=True, null=True)
    
    DRINK_CHOICES = (
                ('1', 'sometimes'),
                ('2', 'rarely'),
                ('3', 'never'),
    )
    drinking = models.CharField(max_length=1, choices=DRINK_CHOICES, blank=True, null=True)

    SMOKE_CHOICES = (
                ('1', 'yes'),
                ('2', 'sometimes'),
                ('3', 'vape'),
                ('4', 'no'),
    )
    smoking = models.CharField(max_length=1, choices=SMOKE_CHOICES, blank=True, null=True)

    SPORT_CHOICES = (
                ('1', 'always'),
                ('2', 'sometimes'),
                ('3', 'rarely'),
                ('4', 'never'),
    )
    sport = models.CharField(max_length=1, choices=SPORT_CHOICES, blank=True, null=True)

    CHILD_CHOICES = (
                ('1', 'already-have'),
                ('2', 'dont-have-but-want'),
                ('3', 'dont-have'),
                ('4', 'childfree'),
    )
    children = models.CharField(max_length=1, choices=CHILD_CHOICES, blank=True, null=True)


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

    
