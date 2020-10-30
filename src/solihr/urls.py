from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from public.views import index

from cvwriting.views import mainCV
from hiring.views import mainHiring

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('jobs/', include('jobs.urls'), name='jobs'),
    path('accounts/', include('allauth.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('cvwriting/', mainCV, name='cvwriting'),
    path('hiring/', mainHiring, name='hiring'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)