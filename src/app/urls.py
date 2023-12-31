"""app URL Configuration

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
from django.urls import path, include
from core.homepage.views import IndexView

from django.conf import settings
from django.conf.urls.static import static

app_name = 'miguel'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path('login/', include('core.login.urls')),
    path('dashboard', include('core.base.urls.dashboard_urls')),
    path('category/', include('core.base.urls.category_urls')),
    path('product/', include('core.base.urls.products_urls')),
    path('client/', include('core.base.urls.client_urls')),
    path('sales/', include('core.base.urls.sale_urls')),
    path('reports/', include('core.reports.urls')),
    path('users/', include('core.user.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
