from django.conf.urls import url
from django.urls import path
from events import views
from .views import Events
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    path('events/', Events.as_view(), name="events")
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)