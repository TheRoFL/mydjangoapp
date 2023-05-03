from django.contrib import admin

from .models import ProfileData
from .models import ProfileLikes


admin.site.register(ProfileData)
admin.site.register(ProfileLikes)
