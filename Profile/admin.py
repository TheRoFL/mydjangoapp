from django.contrib import admin

from .models import ProfileData
from .models import ProfileLikes
from .models import Interests
from .models import PersonalData
    


admin.site.register(ProfileData)
admin.site.register(ProfileLikes)
admin.site.register(Interests)
admin.site.register(PersonalData)