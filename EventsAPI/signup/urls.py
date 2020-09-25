from django.urls import path
from .views import SignupView, SetNewPasswordAPIView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, RequestPasswordResetEmail, LogoutAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('signup/', SignupView.as_view(), name="signup"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
]

















#from django.urls import path
#from .views import Signup, Login, Logout
#from django.conf.urls import url
#from rest_framework.authtoken.views import ObtainAuthToken
#from signup import views

#urlpatterns = [
    #path('signup/', Signup.as_view(), name="signup"),
    #path('login/', Login.as_view(), name="login"),
    #path('logout/', Logout.as_view(), name="logout"),
   # url(r'^api-token-auth/', views.obtain_auth_token)
#]








#
#from django.conf.urls import url
#from signup import views
#from django.urls import path
#from .views import  Login, Logout
#
#urlpatterns = [
#    url(r'^api/signup$', views.user_list),
#    url(r'^api/signup/(?P<pk>[0-9]+)$', views.user_details)
    
    
#]