"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from catalog import views
from catalog.views import health
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# for swagger config
schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation for IMB Catalog",
        default_version='v1',
        description="API documentation for for IMB Catalog",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


# the URLs to access the APIs from the views.py file
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/catalog/products/", views.products_api),
    path("api/catalog/ret/", views.products_api_ret),
    path("api/catalog/update/", views.data_del_up),
    path("api/catalog/src/", views.search),
    path("api/catalog/health/", health, name='health_check'),
    path("api/api-docs", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
