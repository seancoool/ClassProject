from django.db import models
from django.contrib.auth import get_user_model
from apps.users.models import BaseModel
from apps.courses.models import Course


UserProfile = get_user_model()


class UserAsk(BaseModel):
    name = models.CharField(verbose_name="姓名", max_length=20)
    stu_num = models.IntegerField(verbose_name="手机", max_length=11)
    course_name = models.ForeignKey(Course, verbose_name="课程名", on_delete=models.SET_NULL, max_length=50,
                                    null=True, blank=True)

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name


class CourseComment(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    comment = models.CharField(verbose_name="评论", max_length=300)

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name


class UserFavorite(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    fav_id = models.IntegerField(verbose_name="数据id", null=True, blank=True)
    type = models.IntegerField(verbose_name="收藏类型", max_length=300, default=1,
                               choices=((1, '课程'), (2, '课程机构'), (3, '讲师')))

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    message = models.CharField(verbose_name="消息", max_length=200)
    has_read = models.BooleanField(verbose_name="是否已读", default=False)

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name


class UserCourse(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name





