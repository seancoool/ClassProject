import xadmin
from apps.courses.models import *


class CourseAdmin(object):
    list_display = ["name", "teacher", "detail", "degree", "learn_time", "stu_num"]
    search_fields = ["name", "teacher__name", "degree"]
    list_filter = ["name",  "teacher__name", "degree",  "learn_time", "create_time"]
    list_editable = ["name", "teacher", "degree"]


class LessonAdmin(object):
    list_display = ['course', 'name', 'learn_time', 'create_time']
    search_fields = ['course__name', 'name']
    list_filter = ['course__name', 'name', 'learn_time', 'create_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'create_time']
    search_fields = ['lesson__name', 'name']
    list_filter = ['lesson__name', 'name', 'create_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'file', 'create_time']
    search_fields = ['course__name', 'name', 'file']
    list_filter = ['course__name', 'name', 'file', 'create_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
