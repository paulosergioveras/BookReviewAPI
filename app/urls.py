from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Book Review API",
        default_version='v1',
        description="Documentação da API de livros e avaliações",
        terms_of_service="https://github.com/paulosergioveras/BookAPI",
        contact=openapi.Contact(email="paulosergiovc12@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('book.urls')),
    path('api/v1/', include('review.urls')),

    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
