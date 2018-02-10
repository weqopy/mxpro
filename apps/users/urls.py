from django.conf.urls import url

from .views import UserInfoView, UploadImageView, UpdateEmailView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),

    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),

    # 用户个人中心修改密码

    # TODO: 发送过程中邮箱验证失败，通过 debug 获取 code 修改成功
    # 发送邮箱验证码

    # 修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name='update_email'),
]
