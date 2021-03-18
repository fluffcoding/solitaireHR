from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users.views import profile_redirect

from public.views import index, contact_view

from cvwriting.views import mainCV
from hiring.views import mainHiring

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('jobs/', include('jobs.urls'), name='jobs'),
    path('accounts/profile', profile_redirect,name='profile'),
    path('accounts/', include('allauth.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('cvwriting/', mainCV, name='cvwriting'),
    # path('hiring/', mainHiring, name='hiring'),
    path('contact/', contact_view, name='contact'),
    path('api/', include('api.urls'), name='api'),
    path('hiring/', include('hiring.urls'), name='hiring'),
    path('users/', include('users.urls'), name='users'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)