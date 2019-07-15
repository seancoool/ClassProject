from django.db import models
from apps.users.models import BaseModel
from apps.organizations.models import Teacher


"""
1. 设计表结构重要的几点
产生的实体
课程 Course
章节 Lesson
视频 Video
视频资源 CourseResource

实体1 <关系> 实体2
课程   1对多 章节
章节   1对多 视频
课程   1对多 课程资源

2. 实体的具体字段

3. 每个字段的类型是否必填
"""


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="讲师")
    name = models.CharField(verbose_name="课程名", max_length=50)
    description = models.CharField(verbose_name="课程描述", max_length=300)
    learn_time = models.IntegerField(verbose_name="学习时长(分钟数)", default=0)
    stu_num = models.IntegerField(verbose_name="学习人数)", default=0)
    fav_num = models.IntegerField(verbose_name="收藏数)", default=0)
    click_num = models.IntegerField(verbose_name="点击次数)", default=0)
    degree = models.CharField(verbose_name="学习难度)", choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], max_length=2)
    category = models.CharField(verbose_name="课程类别", max_length=20, default=u'后端开发')
    tag = models.CharField(verbose_name="标签", max_length=10, default='')
    cover = models.ImageField(verbose_name="封面", upload_to="courses/%Y/%m", max_length=100)
    need_know = models.CharField(verbose_name="学习须知", max_length=300, default='')
    teacher_tell = models.CharField(verbose_name="老师告诉你", max_length=300, default='')
    detail = models.TextField(verbose_name="课程详情")

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(verbose_name="章节名", max_length=100)
    learn_time = models.IntegerField(verbose_name="学习时长(分钟数)", default=0)

    class Meta:
        verbose_name = "章节信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='章节')
    name = models.CharField(verbose_name="视频名", max_length=50)
    learn_time = models.IntegerField(verbose_name="学习时长(分钟数)", default=0)
    url = models.CharField(verbose_name="地址", max_length=200)

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(verbose_name="名称", max_length=50)
    url = models.CharField(verbose_name="地址", max_length=200)
    file = models.FileField(verbose_name="文件", upload_to="course/resource/%Y/%m", max_length=200)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
