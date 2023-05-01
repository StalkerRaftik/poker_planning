from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

paths = [
    path('api/', include(f'{URLS_PATH}.urls'))
    for URLS_PATH in settings.PROJECT_APPS
]

schema_view = get_schema_view(
    openapi.Info(
        title="pocker API",
        default_version='v1',
    ),
    patterns=[*paths],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/endpoint/',
        TemplateView.as_view(
            template_name='swaggerui/swaggerui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ),
        name='swagger-ui'
    ),
    url(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    *paths
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
