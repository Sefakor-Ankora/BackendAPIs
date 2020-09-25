from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings


schema_view = get_schema_view(
    openapi.Info(
        title="EVENTS MANAGEMENT API",
        default_version='v1',
        description="AZUBI CAPSTONE PROJECT",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="sefakor@outlook.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include('signup.urls')),
        path('api/', include('events.urls')),
        path('api/', include('register.urls')),
        #path('', index, name="index"),
        path('ckeditor/', include('ckeditor_uploader.urls')),
        path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
        
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
