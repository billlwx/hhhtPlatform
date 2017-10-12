"""hhht URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from apo import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from apo import selectUid,deleteUserInfo,mcflush,whitelist
import settings




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',views.index),
    url(r'^tools/$', views.tools),
    url(r'^selectUid/$', selectUid.selectUid),
    url(r'^deleteUserInfo/$', deleteUserInfo.deleteUserInfo),
    url(r'^delete_auth/$', deleteUserInfo.delete_auth),
    url(r'^modifyUserInfo/$', deleteUserInfo.modifyUserInfo),
    url(r'^mcflush/$', mcflush.mcflush),
    url(r'^selectwhitelist/$', whitelist.selectwhitelist),
    url(r'^updatewhitelist/$', whitelist.updatewhitelist),

]

urlpatterns += staticfiles_urlpatterns()

