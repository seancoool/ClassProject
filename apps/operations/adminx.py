import xadmin
from apps.operations.models import *


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'create_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'create_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'create_time']
    search_fields = ['user__username', 'course__name']
    list_filter = ['user__username', 'course__name', 'create_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'type', 'create_time']
    search_fields = ['user__username', 'fav_id', 'type']
    list_filter = ['user__username', 'fav_id', 'type', 'create_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'create_time']
    search_fields = ['user__username', 'message', 'has_read']
    list_filter = ['user__username', 'message', 'has_read', 'create_time']


class CourseCommentAdmin(object):
    list_display = ['user', 'course', 'comment', 'create_time']
    search_fields = ['user__username', 'course__name', 'comment']
    list_filter = ['user__username', 'course__name', 'comment', 'create_time']


xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
