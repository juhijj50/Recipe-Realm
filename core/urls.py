from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *
from django.conf import settings  # Missing import
from django.conf.urls.static import static  # Missing import

urlpatterns = [
    path('', home, name='home'),
    path('recepies/', receipes, name='recepies'),
    path('delete-receipe/<id>/',delete_receipe,name="delete_receipe"),
    path('update-receipe/<id>/',update_receipe,name="update_receipe"),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('success_page/', success_page, name="success_page"),  # Fixed typo
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
