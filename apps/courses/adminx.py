import xadmin
from .models import Course, Lesson, Video, CourseResource, BannerCourse


class LessonInline(object):
    """
    设置课程页面增加添加章节的功能，一层嵌套
    """
    module = Lesson
    extra = 0


class CourseResourceInline(object):
    module = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times',
                    'students', 'favorite_nums', 'click_nums', 'add_time', 'get_zj_nums', 'go_to']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students',
                     'favorite_nums', 'image', 'add_time']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times',
                   'students', 'favorite_nums', 'click_nums', 'add_time']
    # 默认排序设置
    # ordering = ['-click_nums']
    # 只读设置
    # readonly_fields = ['click_nums', 'favorite_nums']
    # 隐藏设置，与只读重复无效
    # exclude = ['click_nums']
    # 在列表页直接进行编辑
    list_editable = ['degree', 'desc']
    # 自动刷新时间设置
    # refresh_times = [3, 5, 10]

    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        # 保存课程时统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times',
                    'students', 'favorite_nums', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students',
                     'favorite_nums', 'image', 'add_time']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times',
                   'students', 'favorite_nums', 'click_nums', 'add_time']

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs



class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    # 'course__name' 表示外键中 name 属性
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
