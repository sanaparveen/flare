"""FlareChat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf import settings
from flare.views import register

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^flare/', include('flare.urls')),
    url(r'^accounts/login', login,{'template_name':'login.html'}, name = 'login'),
    url(r'^accounts/logout',logout,{'next_page': '/flare'}, name = 'logout'),
    url(r'^accounts/register/$', register, name ='register')
]

urlpatterns += static(settings.STATIC_URL)