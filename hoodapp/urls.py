"""hoodapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('hood.urls')),
    path('accounts/register/',
        RegistrationView.as_view(success_url='/accounts/login'),
        name='django_registration_register'),
    # path('accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'^logout/$', views.logout, {"next_page": '/'},name='logout')
]