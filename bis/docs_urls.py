from django.urls import re_path, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="bis API",
        default_version='v1',
    ),
    validators=['ssv'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(
        r'^swagger(?P<format>.json|.yaml)$',
        schema_view.without_ui(cache_timeout=None),
        name='schema-json'
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=None),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=None),
        name='schema-redoc'),
]
