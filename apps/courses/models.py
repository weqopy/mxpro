from datetime import datetime

from django.db import models

from organization.models import CourseOrg, Teacher


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name='课程机构', null=True)
    name = models.CharField(max_length=50, verbose_name='课程名')
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    is_banner = models.BooleanField(default=False, verbose_name='是否轮播')
    degree = models.CharField(choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')),
                              max_length=2, verbose_name='课程难度')
    learn_times = models.IntegerField(default=0, verbose_name='学习时长（分钟数）')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    teacher = models.ForeignKey(
        Teacher, verbose_name='教师', null=True, blank=True)
    favorite_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(null=True, blank=True,
                              upload_to='courses/%Y/%m', verbose_name='封面图')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    category = models.CharField(
        default='后端开发', max_length=20, verbose_name='课程类别')
    tag = models.CharField(default='', verbose_name='课程标签', max_length=10)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    need_know = models.CharField(
        max_length=300, default='', blank=True, verbose_name='课程描述')
    teacher_tell = models.CharField(
        max_length=300, default='', blank=True, verbose_name='老师告诉你')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        return self.lesson_set.all().count()
    # 在对应 adminx.CourseAdmin.list_display 中添加类方法名即可显示
    # short_description 自定义显示标题
    get_zj_nums.short_description = "章节数"

    def go_to(self):
        # 添加 HTML 代码
        # 需要使用 mark_safe
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.python.org'>Python 官网</a>")
    go_to.short_description = "跳转"

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        return self.lesson_set.all()

    def __str__(self):
        # 由于 Lesson.course 为 Course 外键，使用__str__方法可方便显示
        return self.name


class BannerCourse(Course):
    class Meta:
        verbose_name = "轮播课程"
        verbose_name_plural = verbose_name
        proxy = True


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        return self.video_set.all()

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='章节')
    name = models.CharField(max_length=100, verbose_name='视频名')
    url = models.CharField(max_length=200, default='', verbose_name='视频地址')
    video_times = models.IntegerField(default=0, verbose_name='视频长度（分钟数）')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='名称')
    download = models.FileField(upload_to='course/resource/%Y/%m',
                                verbose_name='资源文件', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
