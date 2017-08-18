"""basiclog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from showlog import views as showlog_views
from django.conf.urls.static import static
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^test/api', showlog_views.testapi),
    url(r'^test/setting', showlog_views.setting),
    url(r'^logshow', showlog_views.logshow),
    url(r'^index',showlog_views.index,name='index'),
    url(r'^usergroup',showlog_views.usergroupget,name='usergroup'),
    url(r'^user',showlog_views.userget,name='user'),
    url(r'^mistakelogshow',showlog_views.mistakelogshow,name='mistakelogshow'),
    url(r'^host',showlog_views.hostget,name='host')
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

