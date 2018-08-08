from django.urls import path
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from contact import views
from django.conf.urls.static import static


urlpatterns = [
                path('', include('contact.urls')),
                path(r'^admin/', admin.site.urls),
              ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)