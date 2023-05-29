from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('base.urls')),
    path('profile/', include('Profile.urls')),
    path('acquaintances/', include('Acquaintance.urls')),
    path('chat/', include('Chat.urls')),
    path('map/', include('Map.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
