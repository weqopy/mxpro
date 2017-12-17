from django.apps import AppConfig


# 修改菜单显示
class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = "用户信息"
