from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(

    openapi.Info(

        title="PrepArena API",

        default_version='v1',

        description="API Documentation for PrepArena",

    ),

    public=True,

    permission_classes=[permissions.AllowAny],

)


urlpatterns = [

    path('', views.home, name='home'),
    
    path('admin/', admin.site.urls),

    path('', include('accounts.urls')),

    path('quizzes/', include('quizzes.urls')),

    path('dashboard/', include('dashboard.urls')),

    path('leaderboard/', include('leaderboard.urls')),

    path('api/', include('api.urls')),
    
    path("analytics/", include("analytics_app.urls")),

    path(
        'swagger/',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0
        ),
        name='swagger-ui'
    ),

    path(
        'redoc/',
        schema_view.with_ui(
            'redoc',
            cache_timeout=0
        ),
        name='redoc'
    ),

]

if settings.DEBUG:

    urlpatterns += static(

        settings.MEDIA_URL,

        document_root=settings.MEDIA_ROOT

    )