from django.urls import path, include
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Initial Project',
        default_version='v1',
        description='API documentation for Initial Project',
        contact=openapi.Contact(email='dimmond.pro@gmail.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, )
)

urlpatterns = [
    path('', include('entity.urls')),
    path('token', token_obtain_pair),
    path('token/refresh', token_refresh),
    path('docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
