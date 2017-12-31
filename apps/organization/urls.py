from django.conf.urls import url, include
from .views import OrgView, AddUserAskView


# 在 mxpro.urls 中使用 include
urlpatterns = [
    # 课程机构首页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$',  AddUserAskView.as_view(), name='add_ask'),
]
