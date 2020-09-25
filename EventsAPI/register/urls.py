from django.conf.urls import url
from django.urls import path
from register import views
from .views import Register


urlpatterns = [
    
    path('register/', Register.as_view(), name="register")
]