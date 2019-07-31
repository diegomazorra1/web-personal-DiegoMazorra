"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from apps.core import views as core_views
from apps.portfolio import views as portfolio_views
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name="home"),
    path('inicio', core_views.index, name="home2"),
    path('about', core_views.about, name="about"),
    path('contact/', core_views.contact, name="contact"),
    path('portafolio/', portfolio_views.portafolio, name="portafolio"),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
