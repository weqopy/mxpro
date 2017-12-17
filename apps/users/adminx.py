import xadmin
from xadmin import views
from users.models import EmailVerifyRecord, Banner


# xadmin 后台主题设置
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


# xadmin 页面主题、菜单风格设置
class GlobalSettings(object):
    site_title = "后台管理"
    site_footer = "2017"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'all_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'all_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
