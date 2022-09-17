"""greatkart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include
from greatkart import settings
from django.contrib import admin
from django.urls import path, include
from greatkart import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token

schema_view = get_schema_view(
   openapi.Info(
      title="GreatKart API",
      default_version='v1',
      description="Product Details",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@greatkart.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
    path('product_api/', views.ProductList.as_view()),
    path('product_api/<int:pk>', views.ProductRetrieveUpdateDestroy.as_view()),
    path('category_api/', views.CategoryList.as_view()),
    path('category_api/<int:pk>', views.CategoryRetrieveUpdateDestroy.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('register_api/', views.registration_view),
    path('login_api/', obtain_auth_token),
    path('auth_token/', views.TokenList.as_view()),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
