"""mxpro URL Configuration

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
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin
from mxpro.settings import MEDIA_ROOT
from users.views import LoginView, RegisterView, ActiveView, ForgetPwdView, \
    ResetView, ModifyView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^captcha/', include('captcha.urls')),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^active/(?P<active_code>.*)/$', ActiveView.as_view(), name='active'),
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url(r'^modify_pwd/$', ModifyView.as_view(), name='modify_pwd'),

    # 课程机构 url 配置
    url(r'^org/', include('organization.urls', namespace='org')),

    # 课程相关 url 配置
    url(r'^course/', include('courses.urls', namespace='course')),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # 用户相关 url 配置
    url(r'^users/', include('users.urls', namespace='users')),

]
